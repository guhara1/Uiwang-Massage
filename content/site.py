# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://uiwang-massage.pages.dev"

BRAND = "간다GO 의왕 출장마사지"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# IndexNow 키 — 빌드 시 /{INDEXNOW_KEY}.txt 키 파일이 자동 생성된다.
# 이 키로 Bing·Naver 등 IndexNow 참여 검색엔진에 즉시 색인 통보를 보낸다.
INDEXNOW_KEY = "464663fceff586ea9d093f5d1659397e"

# 사이트 설명(RSS 채널 description)
SITE_DESC = "경기도 의왕시 전지역 방문 출장마사지·홈타이 예약 안내. 대표 행정동·의왕역·생활권별 안내."

# 상단 메뉴 — 하위 메뉴에는 키워드를 과하게 반복하지 않고 지역명·역명 중심으로 표시한다.
# 대표 행정동 5개 + 의왕역 1개 + 생활권 8개 구조(스펙 그대로).
NAV = [
    ("홈", "/", []),
    ("서비스 안내", "/#service", [
        ("출장마사지·홈타이 안내", "/#service"),
        ("의왕시 전지역 방문 안내", "/#coverage"),
        ("예약 전 확인 기준", "/#check"),
    ]),
    ("대표 행정동", "/#areas", [
        ("고천동 출장마사지", "/uiwang/gocheon-dong-chuljangmassage/"),
        ("부곡동 출장마사지", "/uiwang/bugok-dong-chuljangmassage/"),
        ("오전동 출장마사지", "/uiwang/ojeon-dong-chuljangmassage/"),
        ("내손동 출장마사지", "/uiwang/naeson-dong-chuljangmassage/"),
        ("청계동 출장마사지", "/uiwang/cheonggye-dong-chuljangmassage/"),
    ]),
    ("의왕역·생활권", "/#stations", [
        ("의왕역 출장마사지", "/uiwang/uiwang-station-chuljangmassage/"),
        ("의왕시청 인근", "/uiwang/uiwang-cityhall-area-chuljangmassage/"),
        ("왕송호수 인근", "/uiwang/wangsong-lake-area-chuljangmassage/"),
        ("백운호수 인근", "/uiwang/baegun-lake-area-chuljangmassage/"),
        ("내손·포일 생활권", "/uiwang/naeson-poil-area-chuljangmassage/"),
        ("청계·학의 생활권", "/uiwang/cheonggye-hagui-area-chuljangmassage/"),
        ("오전동 생활권", "/uiwang/ojeon-area-chuljangmassage/"),
        ("고천·왕곡 생활권", "/uiwang/gocheon-wanggok-area-chuljangmassage/"),
        ("부곡·월암 생활권", "/uiwang/bugok-woram-area-chuljangmassage/"),
    ]),
    ("예약 안내", "/reservation/", []),
    ("이용 가이드", "/guide/", [
        ("이용 전 확인사항", "/guide/"),
        ("홈타이 이용 가이드", "/hometai/"),
        ("운영자 소개", "/about/"),
    ]),
    ("고객센터", "/support/", [
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("개인정보처리방침", "/support/privacy/"),
    ]),
]
