#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·Naver·Yandex 등 IndexNow 참여 엔진.

표준 라이브러리만 사용한다(추가 설치 불필요).

사용법:
  python3 indexnow.py                  # sitemap.xml 의 모든 URL 통보
  python3 indexnow.py /uiwang/...      # 특정 경로(여러 개 가능) 통보
  python3 indexnow.py https://....     # 전체 URL 직접 지정도 가능

동작:
  https://api.indexnow.org/indexnow 공유 엔드포인트로 제출하면
  Bing·Naver(서치어드바이저)·Yandex·Seznam 등 참여 엔진에 함께 전달된다.
  네이버 전용 엔드포인트로도 한 번 더 보낸다.
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content.site import BASE_URL, INDEXNOW_KEY

BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"

# 공유 엔드포인트 하나면 참여 엔진 전체에 분배되지만,
# 안정성을 위해 네이버 전용 엔드포인트에도 함께 보낸다.
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://searchadvisor.naver.com/indexnow",
    "https://www.bing.com/indexnow",
]


def sitemap_urls():
    path = os.path.join(os.path.dirname(__file__), "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def to_url(arg):
    if arg.startswith("http"):
        return arg
    return BASE + "/" + arg.lstrip("/")


def submit(urls):
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")

    for endpoint in ENDPOINTS:
        req = urllib.request.Request(
            endpoint, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                print(f"  [{resp.status}] {endpoint}")
        except urllib.error.HTTPError as e:
            # 200/202 외 응답도 본문을 확인할 수 있게 출력
            print(f"  [{e.code}] {endpoint} — {e.read().decode('utf-8', 'ignore')[:120]}")
        except Exception as e:  # 네트워크 오류 등
            print(f"  [ERR] {endpoint} — {e}")


def main():
    args = sys.argv[1:]
    urls = [to_url(a) for a in args] if args else sitemap_urls()
    if not urls:
        print("통보할 URL이 없습니다.")
        return
    print(f"IndexNow 제출: {len(urls)}개 URL (host={HOST})")
    for u in urls:
        print("   ·", u)
    submit(urls)
    print("완료.")


if __name__ == "__main__":
    main()
