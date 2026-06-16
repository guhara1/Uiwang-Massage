#!/usr/bin/env python3
"""Google Indexing API 로 URL 색인/갱신 통보.

구글은 IndexNow에 참여하지 않으므로 별도 API를 사용한다.

준비:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 후 JSON 키 다운로드
  3) Search Console 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  4) pip install -r requirements.txt   (google-auth, requests)

사용법:
  GOOGLE_APPLICATION_CREDENTIALS=service-account.json python3 google_index.py
  python3 google_index.py service-account.json /uiwang/...  # 키파일·경로 지정

참고:
  Indexing API는 공식적으로 JobPosting·BroadcastEvent 구조화 페이지를 위한 것이며,
  일반 페이지도 호출은 동작하지만 색인을 보장하지는 않는다. 일반 페이지의 1차 통로는
  IndexNow + 사이트맵 + Search Console 색인 요청이고, 본 스크립트는 보조 수단이다.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content.site import BASE_URL

BASE = BASE_URL.rstrip("/")
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def sitemap_urls():
    path = os.path.join(os.path.dirname(__file__), "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def to_url(arg):
    return arg if arg.startswith("http") else BASE + "/" + arg.lstrip("/")


def main():
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성 누락: pip install -r requirements.txt (google-auth, requests)")

    args = sys.argv[1:]
    cred = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if args and args[0].endswith(".json"):
        cred = args.pop(0)
    if not cred or not os.path.exists(cred):
        sys.exit("서비스 계정 JSON 경로를 GOOGLE_APPLICATION_CREDENTIALS 또는 첫 인자로 지정하세요.")

    urls = [to_url(a) for a in args] if args else sitemap_urls()
    creds = service_account.Credentials.from_service_account_file(cred, scopes=SCOPES)
    session = AuthorizedSession(creds)

    print(f"Google Indexing API 제출: {len(urls)}개 URL")
    ok = 0
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"})
        status = "OK" if r.status_code == 200 else f"FAIL {r.status_code}"
        if r.status_code == 200:
            ok += 1
        print(f"  [{status}] {u}" + ("" if r.status_code == 200 else f" — {r.text[:120]}"))
    print(f"완료: {ok}/{len(urls)} 성공")


if __name__ == "__main__":
    main()
