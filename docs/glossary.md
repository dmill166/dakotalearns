# Glossary

<!-- author_status: dakota-authored | section: full page (edited and approved by Dakota 2026-11-08) -->
<!-- Keep entries A–Z by heading. Every entry must make sense to a first-time visitor arriving from a search engine (rules: cs-teaching STYLE.md, Glossary). -->

Plain-language definitions of terms you'll meet around here, **A–Z**.

!!! tip "Two fast ways to find a term"
    Use the **search** box (top right, or press `/` while on any page of the site) to jump straight to a word; it searches the whole site. On wider screens, the **contents** list on the right of this page is a clickable alphabetical index.

Many of these terms also appear as **dotted underlines** in the lessons; hover (or tap) one for a quick definition in context.

<input type="text" id="glossary-filter" placeholder="🔎 Filter terms on this page…" aria-label="Filter glossary terms" style="width:100%;padding:0.6rem 0.8rem;margin:0.5rem 0 1rem;border:1px solid var(--md-default-fg-color--lighter);border-radius:0.4rem;background:var(--md-default-bg-color);color:var(--md-default-fg-color);font-size:0.9rem;">

<p id="glossary-empty" style="display:none"><em>No terms match your filter.</em></p>

## IDE

**Integrated Development Environment**: an editor bundled with tools to write, run, and debug code in one place (e.g., VS Code, PyCharm). IDLE is a tiny IDE; you'll graduate to a fuller one once the fundamentals are yours.

## IDLE

**Integrated Development and Learning Environment**: the simple code editor and interactive shell that ships *with* Python. It's deliberately bare: no aggressive autocomplete or AI suggestions, which is exactly why it's good for learning. You write code, press **F5** (on a Mac, usually **fn + F5**) or choose **Run → Run Module**, and it runs. It's a common place to start before heavier tools. (It's also a nod to Monty Python's Eric Idle; Python is named after Monty Python's Flying Circus.) Official docs: [IDLE](https://docs.python.org/3/library/idle.html).

## I/O

**Input/Output**: the umbrella term for data going *into* a program (keyboard input, a file on your computer, etc.) and coming back *out* (appearing on-screen, a file output, etc.). When a lesson says "interactive I/O," it means the keyboard-and-screen conversation kind.

## Interpreter

The program that reads your Python code and runs it, line by line. When you "install Python," you're mainly installing the interpreter (the `python` / `python3` command).

## OOP

**Object-Oriented Programming**: a style of programming where you bundle data and the actions that belong with it into "objects." In Python you use objects from day one (even a plain piece of text is one!), long before you learn to define your own kinds.

## Operating system (OS)

The software that runs your computer and everything on it: **Windows**, **macOS**, or **Linux** are the three you'll meet most. Guides often branch by OS ("on Windows do this; on macOS do that") because each one names things a little differently: same destination, slightly different doors.

## PATH

A list your operating system keeps of folders to search when you type a program's name. When a guide says "add Python to your PATH," it means "let me type `python` in a terminal and have the computer find it," instead of typing the program's full location every time. Without it, you'd type something like `C:\Users\you\AppData\Local\Programs\Python\Python314\python.exe` every time you want to run Python; with it, just `python`. The classic Windows gotcha ("`python` is not recognized") is almost always a PATH that doesn't include Python's folder.

A desktop shortcut works because it remembers exactly where one program lives. PATH is the terminal's version of that: instead of one saved location per program, it's a short list of folders your computer checks, in order, whenever you type a program's name.

## REPL

**Read-Eval-Print Loop**: an interactive prompt that **R**eads a line of code, **E**valuates it, **P**rints the result, and **L**oops for the next line. Python's `>>>` prompt (including IDLE's shell) is a REPL: type `2 + 2`, press Enter, see `4`. Great for quick experiments. *Not to be confused with **[Replit](https://replit.com)**, a separate online IDE that happens to share the prefix.*

## RSS

**Really Simple Syndication**: a standard *feed* that lets you follow a site's new or updated posts in a **reader app**, without an account, an algorithm, or email. See [Following the blog (RSS)](guides/following-rss.md) to get new Dakota Learns posts in your reader app.

## Shell

The program that reads the commands you type and runs them: usually **zsh** or **bash** on macOS and Linux, **PowerShell** on Windows. Python has its own shell too: its `>>>` prompt, which runs Python instead of system commands.

## Terminal

The app window where you type commands to your shell: **Terminal** on macOS, **Windows Terminal** on Windows. In everyday talk, "open a terminal" and "open a shell" mean the same thing.

## Virtual environment (venv)

An isolated, per-project set of Python packages, so one project's installs can't clash with another's. You **don't need one** while you're learning the basics with only what ships with Python; you'll want one once your projects start installing outside packages. Official docs: [venv](https://docs.python.org/3/library/venv.html).

---

*Missing a term you'd like defined? Tell me with the feedback link below; this page grows as the lessons do.*
