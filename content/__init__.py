# 전체 페이지 목록 집계
# 1(메인) + 5(대표 행정동) + 1(의왕역) + 8(생활권) + 5(예약/가이드/홈타이/고객센터/개인정보) + 1(운영자 소개)
from . import main, areas, places, info, about

PAGES = [main.PAGE] + areas.PAGES + places.PAGES + info.PAGES + [about.PAGE]
