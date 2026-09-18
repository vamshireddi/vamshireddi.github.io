#!/usr/bin/env python3
"""
Static article builder for vamshireddi.com

  Write:   articles/src/YYYY-MM-DD-your-slug.md   (Markdown + front matter)
  Run:     python3 articles/build.py              (from the repo root, or from articles/)
  Output:  articles/<slug>/index.html             one page per article
           articles/index.html                    listing: search, tag filter, sort, grouped by year
           articles/index.json                    search index (title, summary, tags, text)
           articles/feed.xml                      RSS feed
           sitemap.xml                            home + articles
           index.html                             "Writing" section between the ARTICLES markers

Front matter keys
  title (required)   subtitle   summary (required for previews)   date: YYYY-MM-DD (or YYYY-MM-DD HH:MM)
  updated: YYYY-MM-DD   tags: [A, B]   cover: /articles/images/x.jpg   cover_alt   slug   draft: true
  author (defaults to site author)   toc: true (adds a table of contents from ## headings)

Requires:  pip3 install markdown pygments
"""
import os, re, sys, html, datetime, json
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Missing dependency: run  pip3 install markdown pygments")

ROOT = Path(__file__).resolve().parent          # .../articles
SITE = ROOT.parent                              # repo root
SRC = ROOT / "src"
ART_TEMPLATE = (ROOT / "template.html").read_text(encoding="utf-8")
LIST_TEMPLATE = (ROOT / "list-template.html").read_text(encoding="utf-8")
SITE_URL = "https://vamshireddi.com"
SITE_NAME = "Vamshi Bandaru"
AUTHOR = "Vamshi Krishna Reddy Bandaru"
AUTHOR_BIO = ("Enterprise AI/ML and Salesforce Architect and founder of Godsreality.org "
              "(BibleReal.com, RealApologist.com). Salesforce Certified Systems, Application, "
              "and B2C Solution Architect.")
AUTHOR_LINKEDIN = "https://linkedin.com/in/vamshireddi"
DEFAULT_OG = f"{SITE_URL}/og-image.jpg"
TZ = "-05:00"   # Central Time offset used in machine-readable dates

MD = markdown.Markdown(
    extensions=["extra", "sane_lists", "smarty", "toc", "codehilite", "footnotes"],
    extension_configs={"codehilite": {"noclasses": True, "pygments_style": "monokai"},
                       "toc": {"permalink": False, "toc_depth": "2-3"}})

# ----------------------------------------------------------------- helpers
def parse_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        elif v.lower() in ("true", "false"):
            v = v.lower() == "true"
        else:
            v = v.strip("'\"")
        meta[k.strip()] = v
    return meta, text[m.end():]

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def parse_dt(s):
    s = str(s).strip()
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(s, fmt)
        except ValueError:
            pass
    raise SystemExit(f"Bad date '{s}' — use YYYY-MM-DD or YYYY-MM-DD HH:MM")

def human(dt):
    return dt.strftime("%B %-d, %Y")

def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:00") + TZ

def rfc822(dt):
    return dt.strftime("%a, %d %b %Y %H:%M:00 ") + TZ.replace(":", "")

def words(text):
    return len(re.findall(r"\w+", text))

def strip_tags(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()

def render(template, **kw):
    out = template
    for k, v in kw.items():
        out = out.replace("{{" + k + "}}", "" if v is None else str(v))
    return out

def tag_html(tags, link=True):
    if link:
        return "".join(f'<a class="tag" href="/articles/?tag={html.escape(t)}">{html.escape(t)}</a>' for t in tags)
    return "".join(f'<span class="tag">{html.escape(t)}</span>' for t in tags)

# ----------------------------------------------------------------- load
def load_articles():
    arts = []
    for p in sorted(SRC.glob("*.md")):
        raw = p.read_text(encoding="utf-8")
        meta, body = parse_front_matter(raw)
        if meta.get("draft"):
            print("skip draft", p.name); continue
        if not meta.get("title"):
            sys.exit(f"{p.name}: front matter needs a title")
        fm = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", p.name)
        date = parse_dt(meta.get("date") or (fm.group(1) if fm else None) or
                        datetime.date.fromtimestamp(p.stat().st_mtime).isoformat())
        updated = parse_dt(meta["updated"]) if meta.get("updated") else None
        slug = meta.get("slug") or (fm.group(2) if fm else slugify(meta["title"]))
        MD.reset()
        body_html = MD.convert(body)
        toc = MD.toc if meta.get("toc") and body.count("\n## ") >= 3 else ""
        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]
        n = words(body)
        arts.append(dict(
            slug=slug, title=meta["title"], subtitle=meta.get("subtitle", ""),
            summary=meta.get("summary", ""), date=date, updated=updated,
            tags=tags, cover=meta.get("cover", ""), cover_alt=meta.get("cover_alt", meta["title"]),
            author=meta.get("author", AUTHOR), body=body_html, toc=toc,
            words=n, minutes=max(1, round(n / 220)), text=strip_tags(body_html),
            url=f"{SITE_URL}/articles/{slug}/", path=f"/articles/{slug}/",
        ))
    seen = set()
    for a in arts:
        if a["slug"] in seen:
            sys.exit(f"duplicate slug: {a['slug']}")
        seen.add(a["slug"])
    arts.sort(key=lambda a: a["date"], reverse=True)
    return arts

# ----------------------------------------------------------------- pieces
def card(a):
    cover = (f'<a class="card-cover" href="{a["path"]}"><img src="{html.escape(a["cover"])}" '
             f'alt="{html.escape(a["cover_alt"])}" loading="lazy"></a>') if a["cover"] else ""
    return f'''<article class="card" data-tags="{html.escape("|".join(a["tags"]))}" data-date="{a["date"].isoformat()}" data-slug="{a["slug"]}">
  {cover}
  <div class="card-body">
    <div class="card-meta"><time datetime="{iso(a["date"])}">{human(a["date"])}</time> · {a["minutes"]} min read</div>
    <h2><a href="{a["path"]}">{html.escape(a["title"])}</a></h2>
    <p>{html.escape(a["summary"])}</p>
    <div class="tags">{tag_html(a["tags"])}</div>
  </div>
</article>'''

def related(a, arts, k=3):
    scored = []
    for b in arts:
        if b is a: continue
        shared = len(set(a["tags"]) & set(b["tags"]))
        scored.append((shared, b["date"], b))
    scored.sort(key=lambda t: (t[0], t[1]), reverse=True)
    picks = [b for s, d, b in scored[:k]]
    if not picks: return ""
    items = "".join(f'<li><a href="{b["path"]}">{html.escape(b["title"])}</a><span>{human(b["date"])} · {b["minutes"]} min</span></li>' for b in picks)
    return f'<section class="related"><h2>Related articles</h2><ul>{items}</ul></section>'

# ----------------------------------------------------------------- build
def build():
    arts = load_articles()
    if not arts:
        sys.exit("No articles found in articles/src/")

    for i, a in enumerate(arts):
        newer = arts[i - 1] if i > 0 else None
        older = arts[i + 1] if i + 1 < len(arts) else None
        nav = ""
        if newer or older:
            nav = '<nav class="prevnext">'
            nav += (f'<a class="older" href="{older["path"]}"><span>Older</span>{html.escape(older["title"])}</a>' if older else "<span></span>")
            nav += (f'<a class="newer" href="{newer["path"]}"><span>Newer</span>{html.escape(newer["title"])}</a>' if newer else "<span></span>")
            nav += "</nav>"
        cover_html = (f'<figure class="cover"><img src="{html.escape(a["cover"])}" alt="{html.escape(a["cover_alt"])}"></figure>') if a["cover"] else ""
        og_image = (SITE_URL + a["cover"]) if a["cover"].startswith("/") else (a["cover"] or DEFAULT_OG)
        updated_html = (f'<span class="updated">Updated <time datetime="{iso(a["updated"])}">{human(a["updated"])}</time></span>'
                        if a["updated"] and a["updated"].date() != a["date"].date() else "")
        toc_html = f'<aside class="toc"><div class="toc-title">In this article</div>{a["toc"]}</aside>' if a["toc"] else ""
        page = render(ART_TEMPLATE,
            title=html.escape(a["title"]), subtitle=html.escape(a["subtitle"]),
            description=html.escape(a["summary"]), url=a["url"], og_image=html.escape(og_image),
            date_iso=iso(a["date"]), date_h=human(a["date"]), updated=updated_html,
            minutes=a["minutes"], words=f"{a['words']:,}",
            tags=tag_html(a["tags"]), cover=cover_html, toc=toc_html, body=a["body"],
            author=html.escape(a["author"]), author_bio=AUTHOR_BIO, author_linkedin=AUTHOR_LINKEDIN,
            prevnext=nav, related=related(a, arts),
            share_linkedin=f"https://www.linkedin.com/sharing/share-offsite/?url={a['url']}",
            share_x=f"https://twitter.com/intent/tweet?url={a['url']}&text={html.escape(a['title'])}",
            jsonld=json.dumps({"@context": "https://schema.org", "@type": "BlogPosting",
                "headline": a["title"], "description": a["summary"], "datePublished": iso(a["date"]),
                "dateModified": iso(a["updated"] or a["date"]), "wordCount": a["words"], "keywords": ", ".join(a["tags"]),
                "author": {"@type": "Person", "name": a["author"], "url": SITE_URL},
                "publisher": {"@type": "Person", "name": AUTHOR, "url": SITE_URL},
                "image": og_image, "mainEntityOfPage": a["url"]}),
        )
        out = ROOT / a["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        print("built", out.relative_to(SITE))

    # listing grouped by year
    years = {}
    for a in arts:
        years.setdefault(a["date"].year, []).append(a)
    groups = "".join(f'<section class="year" data-year="{y}"><h2 class="year-title">{y}</h2><div class="cards">'
                     + "\n".join(card(a) for a in arts_y) + "</div></section>"
                     for y, arts_y in sorted(years.items(), reverse=True))
    all_tags = {}
    for a in arts:
        for t in a["tags"]:
            all_tags[t] = all_tags.get(t, 0) + 1
    tag_filters = "".join(f'<button class="chip" data-tag="{html.escape(t)}">{html.escape(t)} <span>{n}</span></button>'
                          for t, n in sorted(all_tags.items(), key=lambda kv: (-kv[1], kv[0].lower())))
    listing = render(LIST_TEMPLATE,
        description="Articles by Vamshi Krishna Reddy Bandaru on Salesforce architecture, applied AI and machine learning, and building software.",
        url=f"{SITE_URL}/articles/", og_image=DEFAULT_OG, count=len(arts), groups=groups, tag_filters=tag_filters,
        jsonld=json.dumps({"@context": "https://schema.org", "@type": "Blog", "name": f"{SITE_NAME} — Articles",
                           "url": f"{SITE_URL}/articles/", "author": {"@type": "Person", "name": AUTHOR}}))
    (ROOT / "index.html").write_text(listing, encoding="utf-8")
    print("built articles/index.html")

    # search index
    (ROOT / "index.json").write_text(json.dumps([{
        "slug": a["slug"], "title": a["title"], "summary": a["summary"], "tags": a["tags"],
        "date": a["date"].isoformat(), "minutes": a["minutes"], "text": a["text"][:20000]} for a in arts],
        ensure_ascii=False), encoding="utf-8")
    print("built articles/index.json")

    # RSS
    items = "".join(f"""
  <item>
    <title>{html.escape(a["title"])}</title>
    <link>{a["url"]}</link>
    <guid isPermaLink="true">{a["url"]}</guid>
    <pubDate>{rfc822(a["date"])}</pubDate>
    <author>{html.escape(a["author"])}</author>{"".join(f"<category>{html.escape(t)}</category>" for t in a["tags"])}
    <description>{html.escape(a["summary"])}</description>
  </item>""" for a in arts)
    (ROOT / "feed.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>
  <title>{SITE_NAME} — Articles</title>
  <link>{SITE_URL}/articles/</link>
  <atom:link href="{SITE_URL}/articles/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Salesforce architecture, applied AI, and building software.</description>
  <lastBuildDate>{rfc822(datetime.datetime.now())}</lastBuildDate>{items}
</channel></rss>
""", encoding="utf-8")
    print("built articles/feed.xml")

    # sitemap
    urls = [(f"{SITE_URL}/", datetime.date.today().isoformat(), "weekly", "1.0"),
            (f"{SITE_URL}/articles/", arts[0]["date"].date().isoformat(), "weekly", "0.8")]
    urls += [(a["url"], (a["updated"] or a["date"]).date().isoformat(), "monthly", "0.7") for a in arts]
    (SITE / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc><lastmod>{m}</lastmod><changefreq>{f}</changefreq><priority>{p}</priority></url>\n" for u, m, f, p in urls)
        + "</urlset>\n", encoding="utf-8")
    print("built sitemap.xml")

    # home page
    home = SITE / "index.html"
    if home.exists():
        h = home.read_text(encoding="utf-8")
        start, end = "<!-- ARTICLES:START -->", "<!-- ARTICLES:END -->"
        if start in h and end in h:
            latest = "\n".join(f'''      <a class="writing-card" href="{a["path"]}">
        <div class="writing-date"><time datetime="{iso(a["date"])}">{human(a["date"])}</time> · {a["minutes"]} min read</div>
        <h3>{html.escape(a["title"])}</h3>
        <p>{html.escape(a["summary"][:170] + ("…" if len(a["summary"]) > 170 else ""))}</p>
        <div class="writing-tags">{"".join(f"<span>{html.escape(t)}</span>" for t in a["tags"][:3])}</div>
      </a>''' for a in arts[:3])
            h = h[:h.index(start) + len(start)] + "\n" + latest + "\n      " + h[h.index(end):]
            home.write_text(h, encoding="utf-8")
            print("updated index.html Writing section")
        else:
            print("note: index.html has no ARTICLES markers; home page not updated")

if __name__ == "__main__":
    build()
