# Portfolio — vamshireddi/vamshireddi.github.io

## Project
Professional portfolio site at `vamshireddi.com` — single-page landing for job market re-entry.

## Structure
```
index.html       ← Portfolio page (single self-contained HTML)
og-image.jpg     ← OG social sharing banner (1200x630)
photo.jpg        ← Professional headshot (400x400)
resume.pdf       ← Downloadable resume
CNAME            ← Custom domain (vamshireddi.com)
```

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
