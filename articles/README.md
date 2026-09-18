# Articles on vamshireddi.com

A zero-dependency-at-runtime article system: you write Markdown, a small Python script turns it into static pages that match the site's dark/gold theme, and GitHub Pages serves them. Each article gets its own URL, Open Graph + JSON-LD metadata (so LinkedIn/X/Google show a proper card), author byline with published/updated dates, reading time and word count, tag links, an optional table of contents, share buttons, related articles (by shared tags), older/newer links, an RSS feed, a sitemap entry, and a spot on the home page. The listing page has full-text search (title, summary, tags, and body), tag filter chips, sort (newest/oldest/title/longest), and year grouping — all client-side, no server.

## Write an article (3 steps)

1. Create `articles/src/YYYY-MM-DD-your-slug.md`. The date prefix orders the list; the slug becomes the URL (`/articles/your-slug/`).
2. Start the file with front matter, then write Markdown:

   ```markdown
   ---
   title: Nine Months as a Student Again
   subtitle: What a UT Austin AI & ML program taught a consultant with no spare time
   date: 2026-09-18
   summary: One or two sentences. Used on the listing page, the home page, and as the LinkedIn/X preview text.
   tags: [AI, Machine Learning, Career]
   cover: /articles/images/pgp-aiml-certificate.jpg
   cover_alt: Describe the image for accessibility
   ---

   First paragraph…

   ## Headings use ##

   Normal Markdown: **bold**, *italic*, [links](https://…), lists, > quotes,
   `code`, fenced code blocks, tables, and images: ![alt](/articles/images/file.jpg)
   ```

   Optional keys: `date: 2026-09-18 08:00` (time is optional), `updated: 2026-10-01` (shows an "Updated" date), `toc: true` (table of contents from `##` headings, when there are 3+), `author:` (defaults to you), `draft: true` (skips the article), `slug: custom-url` (overrides the filename slug).
   Put images in `articles/images/` and reference them with `/articles/images/...`.

3. Build and push:

   ```bash
   cd ~/Projects/vamshireddi.com/site
   python3 articles/build.py        # needs: pip3 install markdown  (once)
   git add -A && git commit -m "Article: your title" && git push origin main
   ```

   Or skip the local build entirely: just commit the `.md` file and push — the GitHub Action in
   `.github/workflows/articles.yml` builds the pages and commits them for you (about a minute).

## What the build produces

| File | Purpose |
|---|---|
| `articles/<slug>/index.html` | The article page |
| `articles/index.html` | Listing of all articles, newest first |
| `articles/index.json` | Search index used by the listing page |
| `articles/feed.xml` | RSS feed |
| `sitemap.xml` | Home + all articles, for search engines |
| `index.html` (home) | The three latest articles injected between `<!-- ARTICLES:START -->` and `<!-- ARTICLES:END -->` in the Writing section |

Generated files are committed to the repo (GitHub Pages serves static files), so never hand-edit them — edit the Markdown and rebuild.

## Changing the look

`articles/template.html` is the article page template and `articles/list-template.html` the listing; both share `articles/articles.css`. `{{title}}`, `{{body}}`, `{{cover}}`, etc. are filled by `build.py`. The CSS at the top of the template mirrors the home page tokens (`--gold`, `--blue`, `--bg-card`), so changing a color there keeps the site consistent. Author bio and site URL live at the top of `build.py`.

## Sharing on LinkedIn

Post the article URL (`https://vamshireddi.com/articles/<slug>/`). LinkedIn reads the `og:image` (the `cover` if set, otherwise `/og-image.jpg`), `og:title`, and `og:description` (the `summary`). If LinkedIn shows a stale preview after you edit, paste the URL into https://www.linkedin.com/post-inspector/ to refresh its cache.
