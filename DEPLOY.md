# Deploy & Domain Setup

<!-- author_status: dakota-authored | section: opening (approved by Dakota 2026-11-09) -->

This is the one-time checklist I followed to get `dakotalearns.com` online. GitHub Pages hosts the built site, and Cloudflare handles DNS (the internet's phone book; it turns the name you type into the address of the server). Set it up once, and from then on every push to `main` redeploys on its own.

<!-- author_status: assistant-shared | section: setup steps, migration plan, hosting options (Dakota's decisions, assistant prose; reviewed by Dakota 2026-11-09) -->

## 0. Prerequisites

- Repo pushed to GitHub as **`dmill166/dakotalearns`** (public).
- Domain **`dakotalearns.com`** registered (Cloudflare Registrar).

## 1. Turn on GitHub Pages (Actions)

1. Push this repo to `main`. The workflow in `.github/workflows/deploy.yml` builds MkDocs and deploys.
2. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Wait for the **Deploy site** workflow to go green (Actions tab). You'll get a `…github.io` URL; confirm the site renders there first.

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

## 4. The one gotcha: keep DNS "grey cloud" during setup

GitHub issues its own Let's Encrypt certificate, and it must be able to see the hostname. So:

- **Set the records to DNS only (grey cloud)** for setup. With Cloudflare's proxy on (orange) + SSL/TLS mode "Flexible," you get redirect loops and cert errors.
- If you later want Cloudflare's CDN/proxy in front: switch the records to proxied **only after** GitHub's cert is active, and set Cloudflare **SSL/TLS → Overview → Full (strict)** (never "Flexible"). For now, grey cloud + GitHub HTTPS is the simplest reliable setup; leave it there unless you have a reason to proxy.

## 5. Verify the domain with GitHub (prevents takeover)

If the Pages site were ever switched off while DNS still points at GitHub, someone else could attach `dakotalearns.com` to their own Pages site. Verifying the domain on your account blocks that.

1. GitHub → your profile **Settings → Pages → Add a domain**, enter `dakotalearns.com`.
2. GitHub shows a **TXT record** (a name like `_github-pages-challenge-dmill166` and a value). Add it in Cloudflare → **DNS → Records** as type **TXT**.
3. Back in GitHub, click **Verify**. Leave the TXT record in place; GitHub re-checks it.

While you're in there: turn on two-factor authentication for both GitHub and Cloudflare (whoever controls either account controls the site), and confirm the domain's transfer lock is on in Cloudflare Registrar.

## 6. Check it works

- `https://dakotalearns.com` loads with a valid padlock.
- `https://www.dakotalearns.com` redirects to the apex (GitHub handles this once both DNS records exist and the apex is set as the custom domain).
- Push a trivial change → Actions runs → site updates in a minute or two.

---

## Posts moved from WordPress

The blog started on `dakotalearns.wordpress.com` in 2022. Every post from it now lives here under `/blog/`, with its text unchanged and its links pointing at this site. The content gate fails any page that still references the old address.

### Where each old post lives now

| Old WordPress post | New home |
|---|---|
| First Post: Blog is Live! (2022-11-19) | `/blog/first-post-blog-is-live/` |
| Virtual Environments: What, Why, How? (2022-11-26) | `/blog/virtual-environments-what-why-how/` |
| Level Up in the Job Market (2022-12-05) | `/blog/level-up-in-the-job-market/` |
| Personal Progress Update #1 (2022-12-12) | `/blog/personal-progress-update-1-2022-12-11/` |
| Life and Loss (2023-01-31) | `/blog/life-and-loss/` |
| Entity Relationship Diagrams (2023-02-06) | `/blog/entity-relationship-diagrams/` |
| Installation Guide for Python: MacOS & Windows (2023-04-03) | `/blog/installation-guide-for-python-macos-windows/` (superseded by [Install Python](docs/guides/install-python.md); the post says so at the top) |
| How to Access Credentials [Securely] in Python (2023-07-03) | `/blog/how-to-access-credentials-securely-in-python-or-not/` |
| Personal Progress Update #2 (2024-03-11) | `/blog/personal-progress-update-2-2024-03-11/` |
| Installation Guide: VS Code (2024-03-25) | `/blog/installation-guide-microsoft-visual-studio-code-vs-code/` |
| Installation Guide: Python 3.x (2024-04-01) | `/blog/installation-guide-python-3-x/` (superseded by [Install Python](docs/guides/install-python.md); the post says so at the top) |
| Learning Python 001: "Hello, World!" and IDLE (2024-04-15) | `/blog/learning-python-001-hello-world-and-idle/` |

---

## Later: optional move to Cloudflare Pages

If you ever want Cloudflare-native hosting (tighter integration with the domain, optional Workers for light dynamic features): in Cloudflare → **Workers & Pages → Create → Pages → Connect to Git**, pick this repo, set **build command** `mkdocs build` and **output directory** `site`, add the custom domain. Same repo, same content: a ~10-minute swap, no rewrite. Not needed now.
