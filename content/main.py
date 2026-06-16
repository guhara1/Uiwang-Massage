# 메인 페이지 — 허브 역할. 모든 키워드를 한 페이지에 밀어 넣지 않고 상세 페이지로 연결한다.
# Schema: WebPage / Organization / FAQPage (실제 오프라인 주소가 없으므로 LocalBusiness 미사용)
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<meta name="naver-site-verification" content="6f26dad9df4c19559cb15e809ff9601edd0b907c" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "의왕 출장마사지·의왕시 홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "inLanguage": "ko-KR",
  "description": "의왕 출장마사지·홈타이 예약 전 대표 동, 의왕역, 이용 기준을 정리한 지역 안내 페이지",
  "isPartOf": {{ "@type": "WebSite", "name": "{BRAND}", "url": "{BASE_URL}/" }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "경기도 의왕시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 의왕시"
  }},
  "contactPoint": {{
    "@type": "ContactPoint",
    "telephone": "{PHONE}",
    "contactType": "reservations",
    "areaServed": "KR",
    "availableLanguage": "Korean"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "의왕시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 고천동, 부곡동, 오전동, 내손동, 청계동 대표 행정동 페이지에서 생활권별 기준을 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "의왕역 근처도 방문되나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "의왕역은 1호선 역세권으로 부곡동·삼동·월암동·초평동 생활권과 함께 의왕역 페이지에서 안내합니다. 정확한 가능 여부는 예약 시 주소를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "내손1동·내손2동은 왜 페이지가 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "내손1동과 내손2동은 같은 생활권이라 내손동 대표 페이지에서 통합 안내합니다. 지역명만 바꿔 비슷한 내용을 반복하는 페이지를 만들지 않기 위함입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "인덕원역 근처도 의왕 사이트에서 다루나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "인덕원역은 행정구역상 안양시에 속해 단독 역세권 페이지를 만들지 않습니다. 청계동·내손동 페이지에서 인덕원 인접 생활권으로 안내합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이와 출장마사지는 무엇이 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "둘 다 자택·숙소·사무실로 방문해 진행하는 방문형 관리입니다. 홈타이는 집에서 받는 방문 관리를 가리키는 표현으로, 예약 절차와 이용 기준은 동일합니다."
      }}
    }}
  ]
}}
</script>"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 의왕시 전지역</p>
    <h1>의왕 출장마사지·의왕시 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/reservation/">예약 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>5개</strong><span>대표 행정동</span></li>
      <li><strong>1개</strong><span>역세권(의왕역)</span></li>
      <li><strong>8개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<p class="lead">의왕 출장마사지를 찾는 분들이 예약 전에 확인하면 좋은 것들을 한 곳에 정리했습니다. 대표 행정동, 의왕역 생활권, 이용 기준을 먼저 보시고 위치에 맞는 페이지로 이동하세요.</p>

<section id="service">
<h2>의왕시에서 출장마사지를 찾는 이유</h2>
<p>의왕 출장마사지를 찾는 사람들은 대부분 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 의왕시는 안양, 군포, 수원, 과천, 성남 생활권 사이에 자리한 도시라 차량 이동과 생활권 이동이 함께 나타나는 지역입니다. 의왕역이 있는 부곡동 생활권은 1호선 접근성이 있고, 고천동과 오전동은 의왕시청과 중심 생활권을 기준으로 움직이며, 내손동과 청계동은 평촌·인덕원·백운호수·포일동·학의동 생활권과 연결되는 성격이 강합니다. {BRAND}는 이런 생활권 차이를 그대로 안내에 반영해, 어느 동에서 예약하시든 방문 기준과 이동 동선을 미리 가늠하실 수 있도록 페이지를 나눠 정리했습니다. 출장마사지와 홈타이는 모두 자택·숙소·사무실 등 머무시는 공간으로 방문해 진행하는 방문형 관리이며, 이 페이지는 의왕시 전체 구조를 설명하는 허브 역할을 합니다.</p>
</section>

<section id="coverage">
<h2>의왕시 전지역 방문 가능 안내</h2>
<p>의왕시 홈타이 사이트를 만들 때 가장 중요한 부분은 행정구를 억지로 만들지 않는 것입니다. 의왕시는 안양처럼 만안구·동안구가 있는 도시도 아니고, 용인처럼 처인구·기흥구·수지구가 있는 도시도 아닙니다. 그래서 이 사이트는 메인페이지 아래에 바로 대표 행정동 페이지를 배치하고, 그 아래 의왕역과 생활권 페이지를 연결하는 구조를 따릅니다. 대표 행정동은 고천동, 부곡동, 오전동, 내손동, 청계동 다섯 곳으로 구성하며, 공식 행정동에 내손1동과 내손2동이 있어도 각각 만들지 않고 내손동 대표 페이지로 통합합니다. 같은 생활권을 잘게 쪼개 비슷한 본문을 반복하는 것보다, 동 단위로 묶어 생활권 특징과 방문 조건을 한 번에 설명하는 편이 이용자에게도 정확하기 때문입니다.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>대표 행정동 페이지는 고천동, 부곡동, 오전동, 내손동, 청계동으로 구성합니다. 각 페이지에서는 해당 동의 생활권 특징, 가까운 거점, 방문 전 확인사항, 예약 가능 시간, 어울리는 이용 상황을 동마다 고유한 내용으로 설명합니다. 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/uiwang/gocheon-dong-chuljangmassage/">고천동 출장마사지</a></li>
<li><a href="/uiwang/bugok-dong-chuljangmassage/">부곡동 출장마사지</a></li>
<li><a href="/uiwang/ojeon-dong-chuljangmassage/">오전동 출장마사지</a></li>
<li><a href="/uiwang/naeson-dong-chuljangmassage/">내손동 출장마사지</a></li>
<li><a href="/uiwang/cheonggye-dong-chuljangmassage/">청계동 출장마사지</a></li>
</ul>
<p>고천동은 의왕시청·왕곡동·고천지구와 이어지는 의왕 중심 행정 생활권이고, 부곡동은 의왕역·삼동·이동·월암동·초평동·왕송호수 생활권을 포괄합니다. 오전동은 모락산 인근 주거지와 고천·호계 사이 이동 동선이 중심이며, 내손동은 계원예대·갈미상가·평촌 인접 생활권, 청계동은 포일동·학의동·백운호수·인덕원 인접 생활권과 연결됩니다.</p>
</section>

<section id="stations">
<h2>의왕역·고천·오전·내손 생활권 안내</h2>
<p>의왕시는 지하철역이 많지 않아 역세권 페이지는 1호선 의왕역 한 곳만 단독으로 운영합니다. 의왕역은 실제로 의왕시 안에 있는 역이라 부곡동·삼동·월암동·초평동 생활권을 연결하기 좋습니다. 그 외 지역은 의왕시청 인근, 왕송호수 인근, 백운호수 인근처럼 실제 이용자가 검색할 만한 생활권 단위로 보조 페이지를 두었습니다.</p>
<ul class="card-grid">
<li><a href="/uiwang/uiwang-station-chuljangmassage/">의왕역 출장마사지</a></li>
<li><a href="/uiwang/uiwang-cityhall-area-chuljangmassage/">의왕시청 인근 출장마사지</a></li>
<li><a href="/uiwang/wangsong-lake-area-chuljangmassage/">왕송호수 인근 출장마사지</a></li>
<li><a href="/uiwang/baegun-lake-area-chuljangmassage/">백운호수 인근 출장마사지</a></li>
<li><a href="/uiwang/naeson-poil-area-chuljangmassage/">내손·포일 생활권 출장마사지</a></li>
<li><a href="/uiwang/cheonggye-hagui-area-chuljangmassage/">청계·학의 생활권 출장마사지</a></li>
<li><a href="/uiwang/ojeon-area-chuljangmassage/">오전동 생활권 출장마사지</a></li>
<li><a href="/uiwang/gocheon-wanggok-area-chuljangmassage/">고천·왕곡 생활권 출장마사지</a></li>
<li><a href="/uiwang/bugok-woram-area-chuljangmassage/">부곡·월암 생활권 출장마사지</a></li>
</ul>
</section>

<section id="rail">
<h2>예정 철도 이슈를 SEO에서 다루는 방식</h2>
<p>의왕에는 개통 전 예정 노선과 예정역 이야기가 많습니다. 다만 개통 전 예정역을 너무 빨리 단독 페이지로 만들면 실제 이용자에게 혼란을 줄 수 있고, 내용이 얇은 페이지가 될 위험도 큽니다. 그래서 이 사이트는 의왕역 한 곳만 단독 역세권 페이지로 두고, GTX-C 의왕역 이슈는 의왕역 페이지 본문에서 보조 설명으로만 다룹니다. 계원예대역 예정은 내손동·포일동 본문에서, 오전역 예정은 오전동 본문에서, 의왕시청역 예정은 고천동·오전동 본문에서 보조 설명으로 처리합니다. 인덕원역은 행정구역상 안양시에 있으므로 의왕 사이트에서 단독 역세권 페이지를 만들지 않고, 청계동·내손동 생활권 안에서 인접 지역으로만 언급합니다.</p>
</section>

<section id="hometai">
<h2>의왕 홈타이 이용 전 확인할 사항</h2>
<p>의왕 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 출장마사지와 홈타이는 부르는 표현이 다를 뿐 방문해서 진행한다는 점은 같고, 예약 절차와 이용 기준도 동일합니다. 처음 이용하신다면 <a href="/hometai/">홈타이 이용 가이드</a>에서 진행 방식과 준비 사항을 먼저 확인하시면 한결 수월합니다. 관리받을 공간에 매트나 침대를 펼 자리가 있는지, 조용한 환경이 가능한지 정도만 확인되면 대부분의 주거 형태에서 받으실 수 있습니다.</p>
</section>

<section id="check">
<h2>예약 전 꼭 확인해야 할 기준</h2>
<p>예약 전에는 방문 가능 지역, 관리 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인하시는 것이 좋습니다. 의왕시는 면적이 아주 큰 편은 아니지만 고천·오전 중심권, 부곡·의왕역 생활권, 내손·청계 생활권의 이동 동선이 서로 다릅니다. 특히 청계동, 학의동, 백운호수 인근은 차량 이동 기준이 중요할 수 있어 추가 이동비와 예약 가능 시간을 미리 확인해 두시면 도착 시간을 정확히 안내받을 수 있습니다. 자세한 절차는 <a href="/reservation/">예약 안내</a>와 <a href="/guide/">이용 전 확인사항</a> 페이지에서 정리했습니다.</p>
</section>

<section id="guide">
<h2>의왕 출장마사지 사이트 이용 가이드</h2>
<p>이 사이트는 과장된 표현 대신 신뢰를 주는 안내형 문장으로 구성했습니다. 메인페이지는 의왕시 전체 안내를 담당하고, 대표 행정동 페이지는 고천동·부곡동·오전동·내손동·청계동 검색을, 의왕역 페이지는 의왕역 검색 의도를, 생활권 페이지는 의왕시청·왕송호수·백운호수·내손/포일·청계/학의처럼 실제 이용자가 찾을 수 있는 지역 검색을 보조합니다. 불법 서비스, 선정적인 표현, 허위 후기, 과도한 할인 문구는 사용하지 않으며, 이용 가능 지역·예약 절차·취소 기준·개인정보 처리 기준·고객 유의사항을 분명하게 보여드리는 것을 원칙으로 합니다. 운영 주체와 콘텐츠 작성 기준은 <a href="/about/">운영자 소개</a>에서 확인하실 수 있습니다.</p>
</section>
""" + PRICING + f"""
<section class="cta">
<h2>예약문의</h2>
<p>방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "의왕 출장마사지｜의왕시 홈타이 지역별 예약 안내",
    "desc": "의왕 출장마사지·홈타이 예약 전 대표 동, 의왕역, 이용 기준을 정리했습니다.",
    "h1": "의왕 출장마사지 · 의왕시 홈타이 지역별 예약 안내",
    "hero": _HERO,
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
}
