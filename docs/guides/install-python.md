# Install Python

Getting Python working is the only setup step before any course — no experience needed.

## What is Python? {#what-is-python}

<!-- author_status: dakota-voice-draft | section: What is Python? (shaped from Dakota's input — his edit) -->
[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is a general-purpose programming language created back in 1991 by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum). I've always found it to be wonderfully user-friendly — something people *with* and *without* a technical background can pick up. It's grown exponentially from its early days into an enterprise-capable tool that fuels everything from personal hobbies to the highly complex systems running inside public and private institutions alike.

I like to use Python to teach computer science for a few reasons:

- **Familiarity:** it's one of the first languages I learned (Java *and* Python, both back in 2012)... so naturally I fell for Python and divorced Java. 😅
- **Readability:** Python *makes* you use whitespace and indentation, which keeps your code readable — for you and for everyone who reads it after you. (Java will happily let you cram a 1,000-line program onto a single line and it'll technically "work"... but no one will like you for it.)
- **Low learning curve:** you don't need to know the nitty-gritty of how computers work to start. Those details help later, as we move into moderate and advanced topics — but whether you're here for an elective credit, because you're bored, or because you want to build something fun like your own [Raspberry Pi home thermometer](https://amzn.to/4xQu45p)[^aff], Python meets you right where you are.

I hope you'll come to like it for these reasons — or for reasons all your own.
<!-- /author_status -->

The full, maintained walk-through (macOS, Windows, Linux), an editor recommendation, a one-command environment check, and troubleshooting lives in the CS 1050 course repository, kept current there so there's a single source of truth:

[:material-github: Module 0 — Set up Python](https://github.com/dmill166/computer-science-1/tree/main/resources/setup){ .md-button .md-button--primary }

## The short version

1. Download the **current** Python from [python.org/downloads](https://www.python.org/downloads/) (the big yellow button) — not an older release.
2. **Windows:** check **"Add python.exe to PATH"** during install. **macOS/Linux:** use the `python3` command.
3. Start in **IDLE** (it ships with Python) — it keeps you focused on concepts instead of leaning on autocomplete.
4. Verify: run `python3 --version` (or `python --version` on Windows). Any 3.13+ is ideal.

You don't need virtual environments or `pyenv` for an intro course — see the full guide for why (and how, if you want them anyway).

## Meet IDLE — the shell and the editor {#meet-idle}

<!-- author_status: dakota-voice-draft | section: IDLE shell & editor primer (drafted for Dakota's edit) -->
When you open **IDLE**, you're actually meeting two tools that work together. Knowing which is which will save you a lot of early confusion, so let's take two minutes here.

### The interactive shell (the `>>>` window)

The first window you see is the **interactive shell**. It's a place where you type **one line, press Enter, and Python answers right away** — a bit like a calculator, or a quick back-and-forth conversation. That `>>>` is Python's prompt; you don't type it, you just type after it.

```pycon
>>> 2 + 2
4
>>> name = "Dakota"
>>> name
'Dakota'
```

Type a value and it echoes back. Store something in a name and Python quietly remembers it. The shell is perfect for **quick experiments** — "wait, what does this do?" — and you'll lean on it constantly. The one catch: it **forgets everything the moment you close it.**

### The editor (where real programs live)

When you want to **keep** your steps and run them again later, you write them in a **file** using IDLE's editor. Open it with **File → New File**, type your program, **save** it with a name ending in `.py` (like `first_program.py`), and run it with **Run → Run Module** (or just **F5**).

One thing that trips people up: **a saved file doesn't echo values back the way the shell does.** In the shell, typing `name` shows you `'Dakota'`; in a file, nothing appears unless you ask for it with `print(...)`. That's not a bug — it's the difference between a conversation (the shell) and a written recipe (a file).

### Which one do I use?

- **Shell** → quick experiments, checking "what does this do?", trying a single line.
- **Editor** → real programs you want to save, re-run, and build on.

You'll bounce between both all the time: start in the shell to play, move to the editor when you're building something to keep.

> **Going deeper (optional):** the [official IDLE documentation](https://docs.python.org/3/library/idle.html) is the complete reference. Fair warning — it's thorough and a bit dense (it's a reference, not a tutorial), so don't feel you need to read it all. It's there for when you want the full details on a menu or shortcut.
<!-- /author_status -->

[^aff]: Affiliate link — if you buy through it, Dakota Learns may earn a small commission at no extra cost to you, which helps keep this work free. [Here's why](../disclaimers.md#affiliate-links); you're always welcome to find it elsewhere.
