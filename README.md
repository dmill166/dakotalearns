# dakotalearns

Source for **[dakotalearns.com](https://dakotalearns.com)** — the public home for Dakota Learns: free, beginner-first computer science taught in public. Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and hosted on GitHub Pages.

## Run it locally

```bash
python3 -m venv .venv && source .venv/bin/activate    # optional
pip install "mkdocs-material==9.7.6"                  # pinned (matches CI)
mkdocs serve        # live preview at http://127.0.0.1:8000
```

Build a static copy into `site/`:

```bash
mkdocs build --strict
```

## Structure

```
dakotalearns/
├── mkdocs.yml                 # site config, theme, nav, plugins
├── docs/                      # all content (MkDocs source)
│   ├── index.md               # landing
│   ├── start-here.md          # newcomer path
│   ├── about.md               # project + licensing + support
│   ├── courses/               # course catalog + per-course hubs
│   │   ├── index.md
│   │   └── cs1050/index.md
│   ├── guides/                # standalone guides (install Python, …)
│   ├── blog/                  # build-in-public posts (Material blog plugin)
│   ├── stylesheets/extra.css  # brand tweaks
│   └── CNAME                  # custom domain (dakotalearns.com)
└── .github/workflows/deploy.yml   # build + deploy to GitHub Pages
```

## Deploying

Pushes to `main` build and deploy automatically (GitHub Actions → Pages). First-time domain + HTTPS setup is in **[DEPLOY.md](DEPLOY.md)**.

## Relationship to the course repos

This site is the **readable front door**. Canonical course materials (syllabus, labs, assignments, starter code) live in their own repos — e.g. [`msudenver-cs1050`](https://github.com/dmill166/msudenver-cs1050). The site links to them and hosts the published, prose versions (lecture articles, blog).

## Licensing

- Content: [CC BY-NC-ND 4.0](LICENSE-CONTENT.md)
- Code: [PolyForm Noncommercial 1.0.0](LICENSE)

Original work only; third-party materials are referenced, not reproduced ([policy](https://github.com/dmill166/cs-teaching/blob/main/COPYRIGHT_POLICY.md)).
