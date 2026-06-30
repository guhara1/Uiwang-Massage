# 내부링크 강화 — 페이지별 '함께 찾는 지역·안내' 블록.
# 인접 생활권/안내 페이지를 롱테일 앵커 텍스트로 연결해 색인과 회유 동선을 강화한다.
# 앵커는 지역명+역명+검색 의도를 담되 과도한 키워드 반복은 피한다.

# path -> [(href, 롱테일 앵커, 보조 설명), ...]
_REL = {
    "": [
        ("/uiwang/gocheon-dong-chuljangmassage/", "고천동 출장마사지 — 의왕시청·왕곡동 생활권", "의왕 행정 중심 생활권 방문 안내"),
        ("/uiwang/uiwang-station-chuljangmassage/", "의왕역 출장마사지 — 부곡·삼동 역세권", "1호선 의왕역 인근 방문 기준"),
        ("/uiwang/naeson-dong-chuljangmassage/", "내손동 출장마사지 — 평촌·인덕원 인접", "계원예대·포일 생활권 안내"),
        ("/hometai/", "의왕 홈타이 이용 가이드", "방문 관리 진행 방식·준비 사항"),
        ("/reservation/", "의왕 출장마사지 예약 안내", "예약 절차·가능 시간 확인"),
        ("/guide/", "이용 전 확인사항", "방문 지역·취소·이동비 기준"),
    ],
    "uiwang/gocheon-dong-chuljangmassage/": [
        ("/uiwang/uiwang-cityhall-area-chuljangmassage/", "의왕시청 인근 출장마사지", "시청 앞 업무·주거 생활권 안내"),
        ("/uiwang/gocheon-wanggok-area-chuljangmassage/", "고천·왕곡 생활권 출장마사지", "왕곡동 포함 넓은 생활권 기준"),
        ("/uiwang/ojeon-dong-chuljangmassage/", "오전동 출장마사지 — 모락산 인근", "고천·호계 사이 이동 동선"),
        ("/uiwang/bugok-dong-chuljangmassage/", "부곡동 출장마사지 — 의왕역 생활권", "1호선 부곡 중심 상가 인근"),
    ],
    "uiwang/bugok-dong-chuljangmassage/": [
        ("/uiwang/uiwang-station-chuljangmassage/", "의왕역 출장마사지 — 1호선 역세권", "부곡·삼동·월암 연결 동선"),
        ("/uiwang/bugok-woram-area-chuljangmassage/", "부곡·월암 생활권 출장마사지", "삼동·초평동 포함 생활권"),
        ("/uiwang/wangsong-lake-area-chuljangmassage/", "왕송호수 인근 출장마사지", "호수 방면 단지 이동 기준"),
        ("/uiwang/gocheon-dong-chuljangmassage/", "고천동 출장마사지 — 의왕시청 생활권", "행정 중심권 방문 안내"),
    ],
    "uiwang/ojeon-dong-chuljangmassage/": [
        ("/uiwang/ojeon-area-chuljangmassage/", "오전동 생활권 출장마사지", "모락산 주거·이동 동선 안내"),
        ("/uiwang/gocheon-dong-chuljangmassage/", "고천동 출장마사지 — 의왕시청 인근", "고천·호계 연결 생활권"),
        ("/uiwang/naeson-dong-chuljangmassage/", "내손동 출장마사지 — 평촌 인접", "계원예대·갈미상가 생활권"),
        ("/uiwang/uiwang-cityhall-area-chuljangmassage/", "의왕시청 인근 출장마사지", "오전동과 이어지는 행정 생활권"),
    ],
    "uiwang/naeson-dong-chuljangmassage/": [
        ("/uiwang/naeson-poil-area-chuljangmassage/", "내손·포일 생활권 출장마사지", "포일자이·평촌 인접 단지 안내"),
        ("/uiwang/cheonggye-dong-chuljangmassage/", "청계동 출장마사지 — 인덕원 인접", "백운호수·학의 생활권 연결"),
        ("/uiwang/cheonggye-hagui-area-chuljangmassage/", "청계·학의 생활권 출장마사지", "학의동 차량 이동 기준"),
        ("/uiwang/ojeon-dong-chuljangmassage/", "오전동 출장마사지", "모락산 인근 주거 생활권"),
    ],
    "uiwang/cheonggye-dong-chuljangmassage/": [
        ("/uiwang/cheonggye-hagui-area-chuljangmassage/", "청계·학의 생활권 출장마사지", "학의동·청계산 인근 안내"),
        ("/uiwang/baegun-lake-area-chuljangmassage/", "백운호수 인근 출장마사지", "포일·학의 방면 차량 동선"),
        ("/uiwang/naeson-dong-chuljangmassage/", "내손동 출장마사지 — 인덕원 인접", "평촌·계원예대 생활권"),
        ("/uiwang/naeson-poil-area-chuljangmassage/", "내손·포일 생활권 출장마사지", "포일동 단지 방문 기준"),
    ],
    "uiwang/uiwang-station-chuljangmassage/": [
        ("/uiwang/bugok-dong-chuljangmassage/", "부곡동 출장마사지 — 의왕역 생활권", "부곡 중심 상가·주거지 안내"),
        ("/uiwang/bugok-woram-area-chuljangmassage/", "부곡·월암 생활권 출장마사지", "삼동·월암·초평동 연결"),
        ("/uiwang/wangsong-lake-area-chuljangmassage/", "왕송호수 인근 출장마사지", "왕송호수·레일파크 방면 단지"),
        ("/uiwang/gocheon-dong-chuljangmassage/", "고천동 출장마사지", "의왕시청 행정 중심 생활권"),
    ],
    "uiwang/uiwang-cityhall-area-chuljangmassage/": [
        ("/uiwang/gocheon-dong-chuljangmassage/", "고천동 출장마사지 — 시청 생활권", "왕곡동 포함 행정 중심권"),
        ("/uiwang/gocheon-wanggok-area-chuljangmassage/", "고천·왕곡 생활권 출장마사지", "고천지구 정비 단지 안내"),
        ("/uiwang/ojeon-dong-chuljangmassage/", "오전동 출장마사지 — 모락산 인근", "시청과 이어지는 주거 생활권"),
        ("/uiwang/uiwang-station-chuljangmassage/", "의왕역 출장마사지", "1호선 역세권 방문 기준"),
    ],
    "uiwang/wangsong-lake-area-chuljangmassage/": [
        ("/uiwang/uiwang-station-chuljangmassage/", "의왕역 출장마사지 — 1호선 역세권", "왕송호수 방면 통근 동선"),
        ("/uiwang/bugok-dong-chuljangmassage/", "부곡동 출장마사지", "부곡 중심 상가·주거 생활권"),
        ("/uiwang/bugok-woram-area-chuljangmassage/", "부곡·월암 생활권 출장마사지", "초평동·월암동 연결 동선"),
        ("/uiwang/gocheon-wanggok-area-chuljangmassage/", "고천·왕곡 생활권 출장마사지", "왕곡동 방면 생활권"),
    ],
    "uiwang/baegun-lake-area-chuljangmassage/": [
        ("/uiwang/cheonggye-dong-chuljangmassage/", "청계동 출장마사지 — 인덕원 인접", "백운호수·학의 생활권"),
        ("/uiwang/cheonggye-hagui-area-chuljangmassage/", "청계·학의 생활권 출장마사지", "학의동 차량 이동 기준"),
        ("/uiwang/naeson-poil-area-chuljangmassage/", "내손·포일 생활권 출장마사지", "포일동 방면 단지 안내"),
        ("/uiwang/naeson-dong-chuljangmassage/", "내손동 출장마사지", "평촌·계원예대 생활권"),
    ],
    "uiwang/naeson-poil-area-chuljangmassage/": [
        ("/uiwang/naeson-dong-chuljangmassage/", "내손동 출장마사지 — 평촌 인접", "계원예대·갈미상가 생활권"),
        ("/uiwang/cheonggye-dong-chuljangmassage/", "청계동 출장마사지", "인덕원·백운호수 인접 생활권"),
        ("/uiwang/baegun-lake-area-chuljangmassage/", "백운호수 인근 출장마사지", "포일·학의 방면 차량 동선"),
        ("/uiwang/cheonggye-hagui-area-chuljangmassage/", "청계·학의 생활권 출장마사지", "학의동 단지 방문 기준"),
    ],
    "uiwang/cheonggye-hagui-area-chuljangmassage/": [
        ("/uiwang/cheonggye-dong-chuljangmassage/", "청계동 출장마사지 — 인덕원 인접", "청계산·백운호수 생활권"),
        ("/uiwang/baegun-lake-area-chuljangmassage/", "백운호수 인근 출장마사지", "포일·학의 방면 차량 동선"),
        ("/uiwang/naeson-dong-chuljangmassage/", "내손동 출장마사지", "평촌·계원예대 생활권"),
        ("/uiwang/naeson-poil-area-chuljangmassage/", "내손·포일 생활권 출장마사지", "포일동 단지 안내"),
    ],
    "uiwang/ojeon-area-chuljangmassage/": [
        ("/uiwang/ojeon-dong-chuljangmassage/", "오전동 출장마사지 — 모락산 인근", "오전동 대표 생활권 안내"),
        ("/uiwang/gocheon-dong-chuljangmassage/", "고천동 출장마사지", "의왕시청 행정 중심 생활권"),
        ("/uiwang/gocheon-wanggok-area-chuljangmassage/", "고천·왕곡 생활권 출장마사지", "고천·호계 연결 동선"),
        ("/uiwang/uiwang-cityhall-area-chuljangmassage/", "의왕시청 인근 출장마사지", "오전동과 이어지는 행정 생활권"),
    ],
    "uiwang/gocheon-wanggok-area-chuljangmassage/": [
        ("/uiwang/gocheon-dong-chuljangmassage/", "고천동 출장마사지 — 의왕시청 인근", "고천 대표 행정 생활권"),
        ("/uiwang/uiwang-cityhall-area-chuljangmassage/", "의왕시청 인근 출장마사지", "시청 앞 업무·주거 생활권"),
        ("/uiwang/ojeon-dong-chuljangmassage/", "오전동 출장마사지", "모락산 인근 이동 동선"),
        ("/uiwang/ojeon-area-chuljangmassage/", "오전동 생활권 출장마사지", "고천·호계 연결 생활권"),
    ],
    "uiwang/bugok-woram-area-chuljangmassage/": [
        ("/uiwang/bugok-dong-chuljangmassage/", "부곡동 출장마사지 — 의왕역 생활권", "부곡 중심 상가·주거지"),
        ("/uiwang/uiwang-station-chuljangmassage/", "의왕역 출장마사지 — 1호선 역세권", "삼동·월암 연결 동선"),
        ("/uiwang/wangsong-lake-area-chuljangmassage/", "왕송호수 인근 출장마사지", "호수 방면 단지 이동 기준"),
        ("/uiwang/gocheon-dong-chuljangmassage/", "고천동 출장마사지", "의왕시청 행정 중심 생활권"),
    ],
    "reservation/": [
        ("/guide/", "이용 전 확인사항", "방문 지역·취소·이동비 기준"),
        ("/hometai/", "의왕 홈타이 이용 가이드", "방문 관리 진행 방식 안내"),
        ("/about/", "운영자 소개", "운영 주체·콘텐츠 작성 기준"),
        ("/uiwang/uiwang-station-chuljangmassage/", "의왕역 출장마사지", "1호선 역세권 방문 기준"),
    ],
    "guide/": [
        ("/reservation/", "의왕 출장마사지 예약 안내", "예약 절차·가능 시간 확인"),
        ("/hometai/", "의왕 홈타이 이용 가이드", "방문 관리 준비 사항"),
        ("/support/", "고객센터·자주 묻는 질문", "1:1 문의·이용 안내"),
        ("/uiwang/gocheon-dong-chuljangmassage/", "고천동 출장마사지", "의왕시청 생활권 방문 안내"),
    ],
    "hometai/": [
        ("/guide/", "이용 전 확인사항", "방문 지역·취소·이동비 기준"),
        ("/reservation/", "의왕 출장마사지 예약 안내", "예약 절차·가능 시간 확인"),
        ("/uiwang/naeson-dong-chuljangmassage/", "내손동 홈타이·출장마사지", "평촌·인덕원 인접 생활권"),
        ("/uiwang/uiwang-station-chuljangmassage/", "의왕역 홈타이·출장마사지", "1호선 역세권 방문 기준"),
    ],
    "support/": [
        ("/guide/", "이용 전 확인사항", "방문 지역·취소·이동비 기준"),
        ("/reservation/", "의왕 출장마사지 예약 안내", "예약 절차·가능 시간 확인"),
        ("/support/privacy/", "개인정보처리방침", "개인정보 수집·이용 기준"),
        ("/about/", "운영자 소개", "운영 주체·작성 기준"),
    ],
    "support/privacy/": [
        ("/support/", "고객센터·자주 묻는 질문", "1:1 문의·이용 안내"),
        ("/guide/", "이용 전 확인사항", "방문 지역·취소 기준"),
        ("/reservation/", "의왕 출장마사지 예약 안내", "예약 절차 확인"),
    ],
    "about/": [
        ("/guide/", "이용 전 확인사항", "방문 지역·취소·이동비 기준"),
        ("/reservation/", "의왕 출장마사지 예약 안내", "예약 절차·가능 시간 확인"),
        ("/support/", "고객센터·자주 묻는 질문", "1:1 문의·이용 안내"),
        ("/hometai/", "의왕 홈타이 이용 가이드", "방문 관리 진행 방식"),
    ],
}


def has_related(path: str) -> bool:
    return path in _REL


def related_section_html(path: str) -> str:
    if path not in _REL:
        return ""
    cards = []
    for href, anchor, blurb in _REL[path]:
        cards.append(
            '<li class="related-card">'
            f'<a href="{href}"><span class="related-anchor">{anchor}</span>'
            f'<span class="related-blurb">{blurb}</span></a>'
            "</li>"
        )
    return (
        '<section class="related" id="related">\n'
        "<h2>함께 찾는 의왕 지역·이용 안내</h2>\n"
        '<p class="related-lead">가까운 생활권과 이용 안내를 함께 확인하시면 방문 가능 여부와 동선을 더 정확히 가늠하실 수 있습니다.</p>\n'
        f'<ul class="related-grid">{"".join(cards)}</ul>\n'
        "</section>\n"
    )
