---
title: dakotalearns — Repo Rules for Agents
scope: repo-local — adds to (and inside this repo, overrides) ~/agents/AGENTS.md
---

<!-- author_status: assistant-shared | section: full page (agent instructions written to Dakota's rules; pending his read) -->

# dakotalearns — Repo Rules for Agents

Source for **[dakotalearns.com](https://dakotalearns.com)** — the public front door for the
CS teaching initiative. MkDocs Material, GitHub Pages. `DEPLOY.md` is the SSOT for shipping.

Course prose is **pulled in** from the course repos by `tools/sync_courses.py`. Those repos are
canonical.

## Hazards

- **Don't edit synced course prose here.** It will be overwritten on the next sync. Fix it in the
  course repo and re-sync.
- **This is Dakota's public voice.** `~/agents/rules/voice.md` applies with full force: the agent
  scaffolds structure, drafts mechanical parts, edits grammar and offers options — it never
  ghost-writes blog posts or course prose.
- **Copyright is a hard line**, same as the course repos. Nothing third-party reproduced.
- **Affiliation disclaimer** must survive any rewrite: independent materials, not affiliated
  with or endorsed by MSU Denver.
- **Pinned dependencies** (`mkdocs-material`, `mkdocs-awesome-nav`) match CI. Don't bump them
  casually — a version drift breaks the build in Actions, not locally.
- `site/` is build output. Never hand-edit it.
- The domain is claimed by `docs/CNAME`; it is also a Google OAuth authorized domain for the
  Workspace MCP consent screen (see `~/agents/rules/google-access.md`). Removing or changing
  the CNAME has consequences beyond this site.
