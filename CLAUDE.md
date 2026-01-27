# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development

```bash
# Install dependencies (if needed - uses system Ruby)
bundle install

# Local development server with live reload
bundle exec jekyll serve

# Build static site to _site/
bundle exec jekyll build
```

The site is hosted on GitHub Pages at kmunk.com. Push to `main` to deploy.

## Architecture

**Jekyll static site** with two main content types:

### Essays (`_posts/`)
- Blog posts about AI, bioethics, technology ethics
- Front matter: `layout: post`, `title`, `date`, `tags`, `excerpt`
- Filename format: `YYYY-MM-DD-slug.md`
- Listed at `/essays/` (see `about.html` which has `permalink: /essays/`)

### Fiction (`_fiction/`)
- Novel chapters using Jekyll collections (see `_config.yml`)
- **Violet novel** in `_fiction/violet/` with 60+ chapters
- Chapters use `layout: chapter` with front matter: `novel`, `chapter` (number), `title`, `act`, `date`
- File prefix numbers (e.g., `011-chapter-01.md`) control sort order
- Support files: `index.md` (novel landing), act markers, glossary, personages, timeline, world-map

### Layouts (`_layouts/`)
- `default.html` - Main site layout with nav, SEO, schema.org structured data
- `minimal.html` - Reduced nav for fiction pages
- `chapter.html` - Chapter layout with prev/next navigation
- `novel.html` - Novel landing page with chapter list
- `post.html` / `page.html` / `home.html` - Standard Jekyll layouts

### Styling
- CSS is inlined in layout files (no external stylesheets)
- Violet novel has custom dark biotech aesthetic in `_fiction/violet/index.md`
- Uses littlefoot.js for footnotes

## Content Conventions

**Posts** should have an `excerpt` for the essays list preview.

**Chapter front matter** example:
```yaml
layout: chapter
novel: Violet
chapter: 1
title: "The Ward, the Princess, and the Sifu"
permalink: /fiction/violet/chapter-01/
act: 1
date: November 02, 2025
```

**Substack export** in `substack-export/` contains chapter markdown formatted for Substack publishing (separate from Jekyll).

## Assets

Images for Violet in `assets/images/violet/` (cover, wordmark SVG, world map).
