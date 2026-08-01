# Terminal Basics (just enough for the course)

<!-- author_status: dakota-voice-draft | section: full page (assistant-drafted 2026-07-21 from Dakota's setup-README 2nd-pass review — review, edit, promote to dakota-authored) -->

The **terminal** (a window where you type commands instead of clicking) shows up a handful of times in this course — checking your Python install, running a self-check script, maybe setting up an optional virtual environment. That's it. You don't need to become a command-line wizard; you need about five commands and one big idea. This could take you somewhere around 10 minutes.

## Opening a terminal

| Your OS | Do this |
|---|---|
| **Windows** | Press the Start key, type `powershell`, press Enter. (Command Prompt works too.) |
| **macOS** | Press `Cmd+Space`, type `terminal`, press Enter. |
| **Linux** | Usually `Ctrl+Alt+T`, or find "Terminal" in your applications menu. |

You'll see a **prompt** — some text ending in something like `$`, `%`, or `>` — waiting for you to type. (This is *your operating system's* prompt, for OS commands. Python's `>>>` shell looks similar but speaks a different language — Python. Type a terminal command at `>>>` and Python will just be confused, and vice versa.)

## The one big idea: your terminal is always *somewhere*

Every terminal window is "standing in" exactly one folder at all times — called the **working directory** (the folder your commands act on). When a guide says *"run this from inside the course folder,"* it means: **walk your terminal into that folder first, then run the command.** Commands like `python3 check_env.py` only find the file if you're standing in the folder that contains it.

## The five commands

| What you want | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Where am I standing? | `pwd` | `pwd` |
| What's in this folder? | `dir` (or `ls`) | `ls` |
| Walk into a folder | `cd Downloads` | `cd Downloads` |
| Jump straight to a folder | `cd C:\Users\you\Downloads` | `cd ~/Downloads` |
| Walk back out (up one level) | `cd ..` | `cd ..` |

Two comfort tips: press **Tab** while typing a folder name and the terminal finishes it for you (this also proves the folder is really there) — and if you ever feel lost, `pwd` tells you where you are. You can't break anything with the five commands above.

## Worked example: running the course's environment check

Say you downloaded `check_env.py` and it landed in your Downloads folder. In my case, on macOS:

```console
$ cd ~/Downloads
$ python3 check_env.py
PASS: Python 3.14.6 (...)
```

On Windows: `cd Downloads`, then `python check_env.py`. The pattern is always the same — **walk to where the file lives, then run it.**

## "Permission denied"? (macOS / Linux, rare)

Our instructions always run scripts *through* an interpreter — `bash setup_env.sh`, `python3 check_env.py` — which needs no special permissions. If some *other* guide ever tells you to run a script directly (`./setup_env.sh`) and you hit `permission denied`, that's the one case where you'd first run `chmod +x setup_env.sh` (mark the file as executable). You won't need it for this course; now you know what it's for anyway.

## When it goes sideways

Errors in the terminal are information, not judgment — everyone's first `cd` typo prints something grumpy. Note your **operating system**, the **exact command you typed**, and the **exact error text**, and bring all three when you ask for help (that trio is what lets anyone diagnose it fast). For course issues, use the feedback link at the bottom of any page or [open an issue](https://github.com/dmill166/computer-science-1/issues).

---

*Next steps: [Install Python](install-python.md) if you haven't yet, or head back to whatever sent you here.*
