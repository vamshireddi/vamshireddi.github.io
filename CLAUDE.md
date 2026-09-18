# Portfolio — vamshireddi/vamshireddi.github.io

## Project
Professional portfolio site at `vamshireddi.com` — single-page landing for job market re-entry.

## Structure
```
index.html       ← Portfolio page (single self-contained HTML)
og-image.jpg     ← OG social sharing banner (1200x630)
photo.jpg        ← Professional headshot (400x400)
Vamshi_Reddy_Bandaru_Resume_2026.pdf ← Downloadable resume (resume.pdf kept as legacy alias)
CNAME            ← Custom domain (vamshireddi.com)
articles/        ← Article system: src/*.md → build.py → <slug>/index.html, index.html, feed.xml (see articles/README.md)
.github/workflows/articles.yml ← builds articles on push when articles/src changes
```

## Articles
- Write Markdown in `articles/src/YYYY-MM-DD-slug.md` with front matter; run `python3 articles/build.py` (pip3 install markdown) or let the GitHub Action build
- Home page Writing section is generated between `<!-- ARTICLES:START/END -->` markers — never hand-edit
- Generated files (articles/<slug>/, articles/index.html, feed.xml) are committed

## Conventions
- Single self-contained HTML file with all CSS/JS inline
- Dark theme with gold (#d4a843) + blue (#4a9eff) accents
- OG + Twitter card meta tags with og-image.jpg?v=4
- Cache-bust OG images with ?v=N query param when updating

## Deployment
- Push to `main` → auto-deploys via GitHub Pages
- Custom domain: vamshireddi.com
- Cloudflare CDN + SSL in front
- CNAME file must stay in repo root

## Links
- /AI/ routes to separate vamshireddi/AI repo

## Rules
- NEVER commit .claude/, memory files, or plan files
- NEVER store API keys, tokens, or credentials
- All content is public — no private/sensitive information in this repo
