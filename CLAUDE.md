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


## Theming (dark + light)
- Both themes come from ONE token block at the top of `index.html` and `articles/articles.css`.
  Dark is the default `:root`; light redefines the same tokens under `:root[data-theme="light"]`
  and under `@media (prefers-color-scheme: light)` for visitors who never touched the toggle.
- **Never write a raw colour in CSS.** Use a token: `var(--text)`, `var(--surface)`, `var(--gold)`,
  and for tints `rgba(var(--gold-rgb), .12)` / `rgba(var(--ov-rgb), .06)`.
- Depth is a token too: cards carry `box-shadow:var(--card-sh)` (none on dark, layered on light)
  and `var(--card-sh-hover)`. Faint panels use `var(--faint-1..3)` (overlay on dark, white on light).
- The toggle lives in the nav (`#themeToggle`); an inline script in `<head>` applies the saved
  choice before first paint so there is no flash. Choice is stored in `localStorage.theme`.
- All text clears WCAG AA (4.5:1) on every surface in both themes — re-check with a contrast
  calculator if you change `--text-*`, `--gold`, `--blue` or `--green`.

## Conventions
- Single self-contained HTML file with all CSS/JS inline
- Dark + light themes, gold (#d4a843) + blue (#4a9eff) accents — see Theming above
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
