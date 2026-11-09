# Terminal Basics (just enough for the course)

<!-- author_status: dakota-authored | section: full page (edited and approved by Dakota 2026-11-08) -->

The **terminal** (a window where you type commands instead of clicking) shows up a handful of times in this course: checking your Python install, running a self-check script, maybe setting up an optional virtual environment. That's it. You don't need to become a command-line wizard; you need about five commands and one big idea. This could take you somewhere around 10 minutes.

## Opening a terminal

| Your OS | Do this |
|---|---|
| **Windows** | Press the Start key, type `powershell`, press Enter. (On Windows 11 it may open inside the Terminal app; that's the same thing.) |
| **macOS** | Press `Cmd+Space`, type `terminal`, press Enter. |
| **Linux** | Usually `Ctrl+Alt+T`, or find "Terminal" in your applications menu. |

You'll see a **prompt** (some text ending in something like `$`, `%`, or `>`) waiting for you to type. (This is *your operating system's* prompt, for OS commands. Python's `>>>` shell looks similar but speaks a different language: Python. Type a terminal command at `>>>` and Python will just be confused, and vice versa.)

## The one big idea: your terminal is always *somewhere*

Every terminal window is "standing in" exactly one folder at all times, called the **working directory** (the folder your commands act on implicitly). When a guide says *"run this from inside the course folder,"* it means: **walk your terminal into that folder first, then run the command.** Commands like `python3 check_env.py` only find the file if you're standing in the folder that contains it. (You can also give the file's full path, like `python3 ~/Downloads/check_env.py`, but walking in first is simpler, and it's what our instructions assume.)

!!! note "`python3` or `python`?"
    On macOS and Linux the command is `python3`. On Windows it's `python`. Wherever a guide shows `python3`, Windows users type `python` instead; everything after it stays the same.

## The five commands

| What you want | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Where am I standing? | `pwd` | `pwd` |
| What's in this folder? | `dir` (or `ls`) | `ls` |
| Walk into a folder | `cd Downloads` | `cd Downloads` |
| Jump straight to a folder | `cd C:\Users\you\Downloads` | `cd ~/Downloads` |
| Walk back out (up one level) | `cd ..` | `cd ..` |

### Finding a folder's full path

The "jump straight to a folder" row needs the folder's full path. Here's how to get it without typing it out by hand:

=== "macOS"

    - In Finder, choose **View → Show Path Bar**. The full path appears along the bottom of the window, one breadcrumb per folder.
    - Or drag the folder onto your Terminal window: its full path appears at the prompt, ready to use.

=== "Windows"

    - In File Explorer, click the address bar at the top of the window. It switches to the full path (like `C:\Users\you\Downloads`), ready to copy.
    - Or drag the folder onto your PowerShell window to paste its path.

=== "Linux"

    - In most file managers, press **Ctrl + L** to show the full path in the location bar.
    - Or drag the folder onto your terminal window to paste its path.

Two comfort tips: press **Tab** while typing a folder name and the terminal finishes it for you (this also proves the folder is really there; if more than one name matches, press Tab again), and if you ever feel lost, `pwd` tells you where you are. You can't break anything with the five commands above.

## Worked example: running the course's environment check

Say you downloaded `check_env.py` and it landed in your Downloads folder. In my case, on macOS:

```console
$ cd ~/Downloads
$ python3 check_env.py
Computer Science 1 environment check
----------------------------------------
Python version : 3.14.6
Interpreter    : /Library/Frameworks/Python.framework/Versions/3.14/bin/python3
Operating sys  : Darwin (arm64)
----------------------------------------

RESULT: PASS - your Python is ready for Computer Science 1.
```

Your version, interpreter path, and operating system lines will differ; the last line is the one that matters.

On Windows: `cd Downloads`, then `python check_env.py`. The pattern is always the same: **walk to where the file lives, then run it.**

## "Permission denied"? (macOS / Linux, rare)

Our instructions always run scripts *through* an [interpreter](../glossary.md#interpreter) (`bash setup_venv.sh`, `python3 check_env.py`) which needs no special permissions. If some *other* guide ever tells you to run a script directly (`./setup_venv.sh`) and you hit `permission denied`, that's the one case where you'd first run `chmod +x setup_venv.sh` (mark the file as executable). You won't need it for this course; now you know what it's for anyway.

## When it goes sideways

Errors in the terminal are information, not judgment; everyone's first `cd` typo prints something grumpy. Gather [your details](#getting-your-details) (your operating system, your shell, your Python version, the exact command you typed, and the exact error text) and bring them when you ask for help. That's what lets anyone diagnose it fast. For course issues, use the feedback link at the bottom of this page.

## Getting your details

When you ask for help, these details let anyone figure out what's going on fast. Your **shell** matters more than you might think: PowerShell, zsh and bash each have their own syntax, so the same command can work in one and fail in another.

=== "macOS"

    - **Operating system and version:** Apple menu → **About This Mac**.
    - **Your shell:** run `echo $SHELL`. On recent Macs it says `/bin/zsh`.
    - **Python version:** run `python3 --version`.

=== "Windows"

    - **Operating system and version:** press **Windows + R**, type `winver`, and press Enter.
    - **Your shell:** a prompt that starts with `PS` (like `PS C:\Users\you>`) means PowerShell; run `$PSVersionTable.PSVersion` for its version. No `PS` at the start (just `C:\Users\you>`) means you've opened Command Prompt by mistake; close it and open PowerShell instead.
    - **Python version:** run `python --version`.

=== "Linux"

    - **Operating system and version:** run `cat /etc/os-release`.
    - **Your shell:** run `echo $SHELL`.
    - **Python version:** run `python3 --version`.

Along with those, copy the **exact command you typed** and the **exact error text**. Copy and paste beats retyping; one changed character can hide the real problem.

---

*Next steps: [Install Python](install-python.md) if you haven't yet, or head back to whatever sent you here.*
