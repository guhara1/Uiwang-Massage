#!/usr/bin/env python3
"""발행 파이프라인 — 빌드 후 검색엔진에 즉시 색인 통보까지 한 번에.

사용법:
  python3 publish.py                 # 빌드 + IndexNow(전체 URL)
  python3 publish.py /uiwang/...     # 빌드 + IndexNow(지정 경로만)

옵션:
  GOOGLE_APPLICATION_CREDENTIALS 가 설정돼 있으면 Google Indexing API 도 함께 호출.

참고: 과거의 sitemap ping(google.com/ping, bing.com/ping)은
      구글·빙 모두 2023년에 폐기되어 더 이상 동작하지 않는다.
      현재 즉시 색인 통보의 표준 경로는 IndexNow(빙·네이버) + Indexing API(구글)다.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
args = sys.argv[1:]


def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    return subprocess.call(cmd, cwd=ROOT)


# 1) 빌드
run([PY, "build.py"])

# 2) IndexNow (Bing·Naver) — 항상 실행, 추가 의존성 없음
run([PY, "indexnow.py", *args])

# 3) Google Indexing API — 서비스 계정이 있을 때만
if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
    run([PY, "google_index.py", *args])
else:
    print("\n(GOOGLE_APPLICATION_CREDENTIALS 미설정 → Google Indexing API 단계 건너뜀)")

print("\n발행 완료.")
