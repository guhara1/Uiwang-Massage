#!/usr/bin/env python3
"""간다GO 의왕 출장마사지 — 정적 사이트 빌드 스크립트.

content/ 패키지의 페이지 정의를 읽어 정적 HTML을 생성한다.

규칙(자동 적용):
  - 본문 텍스트 2,000자 미만 페이지는 robots noindex 처리
  - sitemap.xml 에는 index 허용 페이지만 포함
  - breadcrumb 데이터로 BreadcrumbList JSON-LD 자동 생성
  - 지역+역+테마 조합 경로는 생성 자체가 불가능한 구조
"""
import datetime
import email.utils
import html
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content import PAGES
from content.site import (BASE_URL, BRAND, INDEXNOW_KEY, NAV, PHONE,
                          PHONE_DISPLAY, SITE_DESC)

ROOT = os.path.dirname(os.path.abspath(__file__))
MIN_INDEX_CHARS = 2000


def text_length(body_html: str) -> int:
    """태그를 제거한 본문 글자수(공백 포함, 연속 공백은 1자).
    공통 요금 블록은 페이지 고유 본문이 아니므로 측정에서 제외한다."""
    text = re.sub(r'<section class="pricing">.*?</section>', " ", body_html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


def render_nav(current_path: str) -> str:
    items = []
    for label, href, children in NAV:
        active = " is-active" if href == "/" + current_path else ""
        if children:
            sub = "".join(
                f'<li><a href="{c_href}">{c_label}</a></li>'
                for c_label, c_href in children
            )
            items.append(
                f'<li class="nav-item has-sub{active}">'
                f'<a href="{href}">{label}</a>'
                f'<ul class="sub-menu">{sub}</ul></li>'
            )
        else:
            items.append(
                f'<li class="nav-item{active}"><a href="{href}">{label}</a></li>'
            )
    return "".join(items)


def render_breadcrumb(crumbs) -> str:
    if not crumbs:
        return ""
    parts = ['<nav class="breadcrumb" aria-label="현재 위치"><ol>']
    parts.append('<li><a href="/">홈</a></li>')
    for label, href in crumbs:
        if href:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            parts.append(f"<li><span>{label}</span></li>")
    parts.append("</ol></nav>")
    return "".join(parts)


def breadcrumb_jsonld(crumbs, h1: str) -> str:
    """visual breadcrumb 데이터로 BreadcrumbList 구조화 데이터를 만든다."""
    base = BASE_URL.rstrip("/")
    items = [{"@type": "ListItem", "position": 1, "name": "홈", "item": base + "/"}]
    pos = 2
    for label, href in crumbs:
        entry = {"@type": "ListItem", "position": pos, "name": label}
        if href:
            entry["item"] = base + href
        items.append(entry)
        pos += 1
    # 마지막 항목(현재 페이지)이 링크 없이 들어왔다면 이름을 H1으로 보정
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "\n</script>\n"
    )


def inject_toc(body: str):
    """본문 섹션(h2)에 id를 보장하고 좌측 목차 데이터를 만든다."""
    items = []
    counter = [0]

    def repl(m):
        attrs, title = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            sid = idm.group(1)
            opening = f"<section{attrs}>"
        else:
            counter[0] += 1
            sid = f"sec-{counter[0]}"
            opening = f'<section id="{sid}"{attrs}>'
        label = re.sub(r"<[^>]+>", "", title).strip()
        items.append((sid, label))
        return f"{opening}<h2>{title}</h2>"

    body = re.sub(r"<section([^>]*)>\s*<h2>(.*?)</h2>", repl, body, flags=re.S)
    return body, items


def render_toc(items) -> str:
    if len(items) < 3:
        return ""
    links = "".join(
        f'<li><a href="#{sid}">{label}</a></li>' for sid, label in items
    )
    return (
        '<aside class="page-toc"><nav aria-label="페이지 목차">'
        '<p class="toc-title">목차</p>'
        f"<ul>{links}</ul></nav></aside>"
    )


def render_page(page: dict) -> str:
    path = page["path"]
    title = page["title"]
    desc = page["desc"]
    h1 = page["h1"]
    body = page["body"]
    crumbs = page.get("breadcrumb") or []
    extra_head = page.get("extra_head", "")
    hero = page.get("hero", "")

    chars = text_length(body)
    noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
    robots = (
        '<meta name="robots" content="noindex,follow">'
        if noindex
        else '<meta name="robots" content="index,follow">'
    )
    canonical = BASE_URL.rstrip("/") + "/" + path

    bc_jsonld = breadcrumb_jsonld(crumbs, h1) if crumbs else ""

    # 히어로가 있는 페이지(메인)는 H1을 히어로 안에서 출력한다.
    if hero:
        page_head = hero
    else:
        page_head = ""

    h1_html = "" if hero else f"<h1>{h1}</h1>"

    body, toc_items = inject_toc(body)
    toc_html = render_toc(toc_items)
    layout_cls = "page-layout has-toc" if toc_html else "page-layout"

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{BASE_URL.rstrip('/')}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE_URL.rstrip('/')}/assets/og-image.png">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#0a1120">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{bc_jsonld}{extra_head}</head>
<body>
<header class="site-header">
  <div class="header-accent" aria-hidden="true"></div>
  <div class="header-top">
    <div class="header-inner">
      <a class="brand" href="/"><span class="brand-mark">간</span> <span class="brand-text">{BRAND}</span></a>
      <p class="header-tagline"><span class="tag-gem">◆</span> 의왕시 전지역 방문 관리 <span class="tag-gem">◆</span> 24시간 상담</p>
      <a class="header-call" href="tel:{PHONE}"><span class="call-label">예약전화</span> {PHONE_DISPLAY}</a>
      <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <nav class="main-nav" aria-label="주 메뉴">
    <div class="nav-inner"><ul class="nav-list">{render_nav(path)}</ul></div>
  </nav>
</header>
{page_head}<main class="site-main">
  <div class="container {layout_cls}">
    {toc_html}
    <article class="page-content">
      {render_breadcrumb(crumbs)}
      {h1_html}
      {body}
    </article>
  </div>
</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col footer-about">
      <p class="footer-brand">{BRAND}</p>
      <p class="footer-desc">의왕시 전지역 방문 출장마사지·홈타이 안내 사이트입니다. 모든 서비스는 안내된 관리 범위와 위생·안전 기준 안에서만 제공됩니다.</p>
      <address class="footer-contact">
        <span class="footer-contact-row"><span class="footer-label">예약전화</span> <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></span>
        <span class="footer-contact-row"><span class="footer-label">상담시간</span> 연중무휴 24시간</span>
        <span class="footer-contact-row"><span class="footer-label">서비스 지역</span> 경기도 의왕시 전지역</span>
      </address>
    </div>
    <nav class="footer-col" aria-label="지역 안내">
      <p class="footer-title">대표 행정동</p>
      <ul>
        <li><a href="/uiwang/gocheon-dong-chuljangmassage/">고천동 출장마사지</a></li>
        <li><a href="/uiwang/bugok-dong-chuljangmassage/">부곡동 출장마사지</a></li>
        <li><a href="/uiwang/ojeon-dong-chuljangmassage/">오전동 출장마사지</a></li>
        <li><a href="/uiwang/naeson-dong-chuljangmassage/">내손동 출장마사지</a></li>
        <li><a href="/uiwang/cheonggye-dong-chuljangmassage/">청계동 출장마사지</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="역세권·생활권 안내">
      <p class="footer-title">의왕역·생활권</p>
      <ul>
        <li><a href="/uiwang/uiwang-station-chuljangmassage/">의왕역 출장마사지</a></li>
        <li><a href="/uiwang/uiwang-cityhall-area-chuljangmassage/">의왕시청 인근</a></li>
        <li><a href="/uiwang/wangsong-lake-area-chuljangmassage/">왕송호수 인근</a></li>
        <li><a href="/uiwang/baegun-lake-area-chuljangmassage/">백운호수 인근</a></li>
        <li><a href="/uiwang/naeson-poil-area-chuljangmassage/">내손·포일 생활권</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="이용 안내">
      <p class="footer-title">이용 안내</p>
      <ul>
        <li><a href="/reservation/">예약 안내</a></li>
        <li><a href="/guide/">이용 전 확인사항</a></li>
        <li><a href="/hometai/">홈타이 이용 가이드</a></li>
        <li><a href="/about/">운영자 소개</a></li>
        <li><a href="/support/">고객센터</a></li>
        <li><a href="/support/privacy/">개인정보처리방침</a></li>
      </ul>
    </nav>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <p class="footer-copy">&copy; {BRAND}. All rights reserved.</p>
      <p class="footer-note">건전한 방문 관리 서비스를 운영하며, 불법적인 요청은 어떤 경우에도 응하지 않습니다.</p>
    </div>
  </div>
</footer>
<a class="call-fab" href="tel:{PHONE}" aria-label="전화 예약 {PHONE_DISPLAY}">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
  <span class="call-fab-label">예약 전화</span>
</a>
<script src="/assets/nav.js"></script>
</body>
</html>
"""


def build() -> None:
    report = []
    sitemap_urls = []

    for page in PAGES:
        path = page["path"]  # "" 또는 "uiwang/gocheon-dong-chuljangmassage/" 형태
        out_dir = os.path.join(ROOT, path)
        os.makedirs(out_dir, exist_ok=True)
        html_out = render_page(page)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)

        chars = text_length(page["body"])
        noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
        if not noindex:
            sitemap_urls.append({
                "url": BASE_URL.rstrip("/") + "/" + path,
                "title": page["title"],
                "desc": page["desc"],
            })
        report.append((path or "/", chars, "noindex" if noindex else "index"))

    base = BASE_URL.rstrip("/")
    today = datetime.date.today().isoformat()
    now_rfc822 = email.utils.formatdate(usegmt=True)

    # sitemap.xml — lastmod / changefreq / priority 포함
    rows = []
    for item in sitemap_urls:
        is_home = item["url"].rstrip("/") == base
        priority = "1.0" if is_home else "0.8"
        changefreq = "weekly" if is_home else "monthly"
        rows.append(
            "  <url>\n"
            f"    <loc>{item['url']}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>{changefreq}</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            "  </url>"
        )
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(rows)
            + "\n</urlset>\n"
        )

    # rss.xml — 색인 대상 페이지를 RSS 2.0 피드로 발행
    items = []
    for item in sitemap_urls:
        items.append(
            "    <item>\n"
            f"      <title>{html.escape(item['title'])}</title>\n"
            f"      <link>{item['url']}</link>\n"
            f"      <guid isPermaLink=\"true\">{item['url']}</guid>\n"
            f"      <description>{html.escape(item['desc'])}</description>\n"
            f"      <pubDate>{now_rfc822}</pubDate>\n"
            "    </item>"
        )
    with open(os.path.join(ROOT, "rss.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
            "  <channel>\n"
            f"    <title>{html.escape(BRAND)}</title>\n"
            f"    <link>{base}/</link>\n"
            f"    <atom:link href=\"{base}/rss.xml\" rel=\"self\" type=\"application/rss+xml\" />\n"
            f"    <description>{html.escape(SITE_DESC)}</description>\n"
            "    <language>ko-KR</language>\n"
            f"    <lastBuildDate>{now_rfc822}</lastBuildDate>\n"
            + "\n".join(items)
            + "\n  </channel>\n</rss>\n"
        )

    # robots.txt — 주요 검색엔진(구글·네이버 Yeti·빙) 명시 + sitemap/rss
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(
            "User-agent: Googlebot\nAllow: /\n\n"
            "User-agent: Yeti\nAllow: /\n\n"
            "User-agent: bingbot\nAllow: /\n\n"
            "User-agent: Daumoa\nAllow: /\n\n"
            "User-agent: *\nAllow: /\n\n"
            f"Sitemap: {base}/sitemap.xml\n"
            f"Sitemap: {base}/rss.xml\n"
        )

    # IndexNow 키 파일 — /{key}.txt 는 키 문자열만 담는다.
    with open(os.path.join(ROOT, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY + "\n")

    # .nojekyll (GitHub Pages 호환)
    open(os.path.join(ROOT, ".nojekyll"), "w").close()

    width = max(len(p) for p, _, _ in report)
    print(f"{'PATH'.ljust(width)}  CHARS  ROBOTS")
    for p, c, r in sorted(report):
        flag = "" if (r == "noindex" or MIN_INDEX_CHARS <= c) else "  ⚠ thin"
        print(f"{p.ljust(width)}  {str(c).rjust(5)}  {r}{flag}")
    print(f"\n{len(report)} pages built, {len(sitemap_urls)} in sitemap/rss.")
    print(f"sitemap.xml · rss.xml · robots.txt · {INDEXNOW_KEY}.txt 생성 완료.")


if __name__ == "__main__":
    build()
