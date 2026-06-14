# Deploy & Domain Setup

How `dakotalearns.com` gets online: GitHub Pages hosts the built site; Cloudflare serves DNS. One-time setup, then every push to `main` redeploys automatically.

## 0. Prerequisites

- Repo pushed to GitHub as **`dmill166/dakotalearns`** (public).
- Domain **`dakotalearns.com`** registered (Cloudflare Registrar).

## 1. Turn on GitHub Pages (Actions)

1. Push this repo to `main`. The workflow in `.github/workflows/deploy.yml` builds MkDocs and deploys.
2. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Wait for the **Deploy site** workflow to go green (Actions tab). You'll get a `…github.io` URL — confirm the site renders there first.

## 2. Point the domain (Cloudflare DNS)

In the Cloudflare dashboard for `dakotalearns.com` → **DNS → Records**, add:

| Type | Name | Target | Proxy |
|---|---|---|---|
| CNAME | `dakotalearns.com` (apex / `@`) | `dmill166.github.io` | **DNS only (grey cloud)** |
| CNAME | `www` | `dmill166.github.io` | **DNS only (grey cloud)** |

Cloudflare auto-flattens the apex CNAME, so this works without A records. (If you prefer A records instead of the apex CNAME, use GitHub's IPs: `185.199.108.153`, `.109.153`, `.110.153`, `.111.153`, plus AAAA `2606:50c0:8000::153` … `8003::153`.)

## 3. Custom domain + HTTPS on GitHub

1. Repo **Settings → Pages → Custom domain →** enter `dakotalearns.com` → **Save**. (`docs/CNAME` already pins this; the build copies it to the site root.)
2. Wait for the **DNS check** to pass and GitHub to provision the TLS certificate (minutes, occasionally up to ~an hour).
3. Tick **Enforce HTTPS**.

## 4. The one gotcha — keep DNS "grey cloud" during setup

GitHub issues its own Let's Encrypt certificate, and it must be able to see the hostname. So:

- **Set the records to DNS only (grey cloud)** for setup. With Cloudflare's proxy on (orange) + SSL/TLS mode "Flexible," you get redirect loops and cert errors.
- If you later want Cloudflare's CDN/proxy in front: switch the records to proxied **only after** GitHub's cert is active, and set Cloudflare **SSL/TLS → Overview → Full (strict)** (never "Flexible"). For now, grey cloud + GitHub HTTPS is the simplest reliable setup — leave it there unless you have a reason to proxy.

## 5. Verify

- `https://dakotalearns.com` loads with a valid padlock.
- `https://www.dakotalearns.com` redirects to the apex (GitHub handles this once both DNS records exist and the apex is set as the custom domain).
- Push a trivial change → Actions runs → site updates in a minute or two.

---

## WordPress migration / redirect plan

The existing posts live on the free `dakotalearns.wordpress.com`. The free tier **cannot** do server-side 301 redirects or custom canonical tags, so the plan is link-based and SEO-friendly:

1. **Don't delete anything** — old posts carry backlinks and search history.
2. **Inventory** every post into the table below.
3. **Classify each:**
   - **Keep** — still fine as-is; just add a footer linking to the new home.
   - **Supersede** — rewrite a current, canonical version here on `dakotalearns.com`; then edit the *old* WordPress post to add a note at the very top: *"📌 Updated version: https://dakotalearns.com/…"*. Search engines and readers follow the link; authority gradually shifts to the new domain.
   - **Retire** — rare; only if truly obsolete. Even then, redirect-by-note rather than delete.
4. As inbound links and new posts accumulate on the owned domain, it becomes the canonical home without ever breaking the old URLs.

### Migration tracker

| Old WordPress URL | New URL on dakotalearns.com | Action (Keep / Supersede / Retire) | Done |
|---|---|---|---|
| /2024/04/01/installation-guide-python-3-x… | /guides/install-python/ | Supersede (Module 0 is the canonical install guide) | ☐ |
| /2023/04/03/installation-guide-for-python-macos-windows… | /guides/install-python/ | Supersede | ☐ |
| _(install guide for VS Code)_ | _(future guide)_ | Keep / later | ☐ |
| _(ERD post)_ | _(future DB course/guide)_ | Keep | ☐ |
| _(remaining posts — fill in)_ | | | ☐ |

> First pass: just the two Python install guides → point them at `/guides/install-python/`. The rest can migrate lazily.

---

## Later: optional move to Cloudflare Pages

If you ever want Cloudflare-native hosting (tighter integration with the domain, optional Workers for light dynamic features): in Cloudflare → **Workers & Pages → Create → Pages → Connect to Git**, pick this repo, set **build command** `mkdocs build` and **output directory** `site`, add the custom domain. Same repo, same content — a ~10-minute swap, no rewrite. Not needed now.
