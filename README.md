# 간다GO 의왕 출장마사지 — 의왕시 홈타이 지역 SEO 사이트

경기도 의왕시 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719** (상호: 간다GO)

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap·BreadcrumbList JSON-LD)
content/
  site.py           # 상호·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ WebPage/Organization/FAQPage JSON-LD)
  areas.py          # 대표 행정동 5개 (고천·부곡·오전·내손·청계)
  places.py         # 의왕역 1개 + 생활권·주요 거점 8개
  info.py           # 예약 안내·이용 전 확인사항·홈타이 가이드·고객센터·개인정보처리방침
  about.py          # 운영자 소개 (E-E-A-T)
  pricing.py        # 코스별 요금 공용 컴포넌트
assets/             # CSS, 모바일 내비 JS, 아이콘
```

## 페이지 구성 (스펙 기준)

| 구분 | 개수 | 비고 |
|------|------|------|
| 메인 | 1 | `/` (의왕 출장마사지·홈타이 허브) |
| 대표 행정동 | 5 | 고천·부곡·오전·내손·청계 |
| 역세권 | 1 | 의왕역 (1호선) |
| 생활권·거점 | 8 | 의왕시청·왕송호수·백운호수·내손포일·청계학의·오전·고천왕곡·부곡월암 |
| 이용 안내 | 5 | 예약 안내·이용 전 확인사항·홈타이 가이드·고객센터·개인정보처리방침 |
| 운영자 소개 | 1 | E-E-A-T (Who/How/Why) |

> 내손1·2동은 내손동으로 통합, 지하철역은 의왕역 1개만 단독 생성,
> 계원예대역·오전역·의왕시청역·GTX-C·인덕원역(안양시)은 단독 색인 페이지 없이 본문 보조 설명으로만 처리.

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다. 본문 2,000자 미만 페이지는
자동으로 `noindex` 처리되고 `sitemap.xml`에서 제외됩니다.

## 색인(인덱싱) 자동화

빌드 시 색인용 파일이 모두 자동 생성됩니다.

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | 색인 페이지 목록 (lastmod·changefreq·priority 포함) |
| `rss.xml` | RSS 2.0 피드 (네이버 RSS 제출·구독용) |
| `robots.txt` | 구글·네이버(Yeti)·빙·다음 명시 + sitemap·rss 위치 |
| `<KEY>.txt` | IndexNow 키 파일 (`content/site.py`의 `INDEXNOW_KEY`) |

### 즉시 색인 통보 스크립트

```bash
python3 publish.py            # 빌드 + IndexNow 전체 URL 통보 (+ 설정 시 Google)
python3 publish.py /uiwang/cheonggye-dong-chuljangmassage/   # 특정 글만 통보
python3 indexnow.py           # IndexNow 단독 실행 (빙·네이버, 의존성 없음)
```

- **IndexNow** (`indexnow.py`): 표준 라이브러리만 사용. `api.indexnow.org`(공유)·
  네이버·빙 엔드포인트로 제출 → **빙·네이버·얀덱스**에 즉시 통보됩니다.
  ⚠️ 키 파일(`/<KEY>.txt`)이 **배포 사이트에 먼저 올라가 있어야** 통보가 검증됩니다.
  (배포 → 그다음 `indexnow.py` 실행)
- **Google Indexing API** (`google_index.py`): 구글은 IndexNow 미참여라 별도 API 사용.
  서비스 계정 JSON + Search Console 소유자 등록 필요. `pip install -r requirements.txt` 후
  `GOOGLE_APPLICATION_CREDENTIALS=키.json python3 google_index.py`.
- **sitemap ping**: `google.com/ping`·`bing.com/ping`은 2023년 폐기되어 동작하지 않습니다.
  현재 표준 경로는 IndexNow(빙·네이버) + Indexing API(구글) + 서치콘솔/서치어드바이저 사이트맵 제출입니다.

### 최초 1회 등록 절차

1. 사이트를 `uiwang-massage.netlify.app`에 배포 (키 파일·sitemap·rss 포함 확인)
2. **네이버 서치어드바이저**: 사이트 인증(메타태그 완료) → 사이트맵 `…/sitemap.xml`,
   RSS `…/rss.xml` 제출 → IndexNow는 `indexnow.py`로 통보
3. **구글 서치콘솔**: 속성 추가 → 사이트맵 `…/sitemap.xml` 제출 → URL 검사로 색인 요청
4. 이후 콘텐츠를 수정할 때마다 `python3 publish.py [경로]` 한 줄이면 빌드 + 즉시 통보 완료

## 배포 전 확인

- `content/site.py`의 `BASE_URL`을 실제 배포 도메인으로 변경한 뒤 다시 빌드하세요.
  (canonical / og:url / sitemap / JSON-LD 절대주소가 모두 이 값을 따릅니다.)
- LocalBusiness 스키마는 실제 오프라인 사업장 주소가 없어 사용하지 않습니다.
  (Organization + WebPage + FAQPage + BreadcrumbList 만 사용)
