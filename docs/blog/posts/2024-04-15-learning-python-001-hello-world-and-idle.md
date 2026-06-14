---
date: 2024-04-15
slug: learning-python-001-hello-world-and-idle
categories:
  - Tutorials
tags:
  - Python
  - IDLE
---

# Learning Python 001: "Hello, World!" and IDLE

Welcome back! I'm very excited to share the following blog post with all of you as the first in a series titled "Learning Python". I've had the idea for a couple of years now and am so elated that the time is finally right to get this series started! This series will focus on building up your knowledge of the Python programming language assuming you have no prior programming experience but are wanting/willing to learn. It'll build sequentially (so post #100 will be harder than post #001), but some posts closer together in numbering may have similar level of content.

<!-- more -->

Rather than waste any more time, let's get right into it - "Learning Python 001: "Hello, World!" and IDLE"!

1. [🔙 Previous Blog Post(s)](https://dakotalearns.wordpress.com/2024/04/15/learning-python-001-hello-world-and-idle/#previous-blog-post-s)
2. [⁉️ IDLE (I thought it was IDE?)](https://dakotalearns.wordpress.com/2024/04/15/learning-python-001-hello-world-and-idle/#idle-i-thought-it-was-ide)
3. [🔢 Numeric Operators in Python](https://dakotalearns.wordpress.com/2024/04/15/learning-python-001-hello-world-and-idle/#numeric-operators-in-python)
4. [💁‍♂️ Rite of Passage ("Hello, World!")](https://dakotalearns.wordpress.com/2024/04/15/learning-python-001-hello-world-and-idle/#rite-of-passage-hello-world)
5. [💭 Thoughts from SkyNet](https://dakotalearns.wordpress.com/2024/04/15/learning-python-001-hello-world-and-idle/#thoughts-from-skynet)
6. [📒 Summary/Links](https://dakotalearns.wordpress.com/2024/04/15/learning-python-001-hello-world-and-idle/#summary-links)
   1. [Summary](https://dakotalearns.wordpress.com/2024/04/15/learning-python-001-hello-world-and-idle/#summary)
   2. [Links](https://dakotalearns.wordpress.com/2024/04/15/learning-python-001-hello-world-and-idle/#links)
7. [✅ Conclusions](https://dakotalearns.wordpress.com/2024/04/15/learning-python-001-hello-world-and-idle/#conclusions)

## 🔙 Previous Blog Post(s)

This guide is intended to follow my last two posts on [Installing Visual Studio Code](https://dakotalearns.wordpress.com/2024/03/25/installation-guide-microsoft-visual-studio-code-vs-code/) and [Installing Python 3.x](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-%f0%9f%90%8d/). If you haven't read those, I'd highly encourage you to start with those so that you 1) Have an IDE installed for your own Python coding progress and 2) Have Python installed (an understandably necessary pre-requisite for this post on learning to code within Python).

## ⁉️ IDLE (I thought it was IDE?)

If you've been following my posts for some time now, I talk about this concept of 'IDE's, or Integrated Development Environments, across a couple of them; so why the heck am I bringing up IDLE?

[Python IDLE](https://docs.python.org/3/library/idle.html), or Integrated Development and Learning Environment, is a Python IDE shipping with the Python default installation (or customized installation, if selected) from [Python.org](https://www.python.org/). It comes with a Shell-like environment that lets you pass individual Python statements and get immediate response, or 'feedback' if you will. In addition, it includes its own text editor with features such as Intelli-sense, Python syntax coloring, and cross-platform support across Windows, Unix, and MacOS.

If it comes with all these things, I just KNOW you're wondering why I wrote a previous guide on installing Visual Studio Code. While I enjoy IDLE for small scripts or quick interaction to test function outputs, I prefer other applications (such as [Microsoft's Visual Studio Code](https://code.visualstudio.com/) or [Jetbrains PyCharm](https://www.jetbrains.com/pycharm/)) for my personal and professional coding efforts. The choice will ultimately be yours as there are many ways to type and debug code but only one that will match your personal style. Let this explanation be one of many you should consider when choosing the right tools for the job.

To launch IDLE, simply search your Windows apps, Mac Spotlight, or other mechanism for the IDLE application. The resulting application that opens should be similar to this:

![](https://dakotalearns.wordpress.com/wp-content/uploads/2024/04/image.png?w=1024)

## 🔢 Numeric Operators in Python

The ">>> " signifies that the IDLE application is waiting on some input from you. Let's see if it's 'smarter than a 5th grader' with some various arithmetic.

![](https://dakotalearns.wordpress.com/wp-content/uploads/2024/04/image-1.png?w=1024)

Wow, that IDLE sure knows its mathematics! This also serves as a good summary of [most of the simple mathematical operations available in Python](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex). Be sure to take careful note of this as we'll be using these in future blog posts / practice problems! Once more to explain these expressions:

|  |  |
| --- | --- |
| Operation | Meaning |
| `x + y` | Sum of `x` and `y` |
| `x - y` | Difference of `x` and `y` |
| `x * y` | Product of `x` and `y` |
| `x / y` | Quotient of `x` and `y` |
| `x // y` | Floored quotient of `x` and `y` |
| `x % y` | Remainder of `x / y` |
| `-x` | The inverse of `x` |
| `+x` | Unchanged `x` |
| `abs(x)` | Absolute value of `x` |
| `int(x)` | Conversion of `x` to an integer |
| `float(x)` | Conversion of `x` to a floating point number |
| `complex(x, y)` | Complex number with real part `x` and imaginary part `y` (`y` defaults to 0) |
| `divmod(x, y)` | The pair `(x // y, x % y)` |
| `pow(x, y)` | `x` to the `y` power |
| `x ** y` | `x` to the `y` power |

Numerical operations and their meaning in Python.

## 💁‍♂️ Rite of Passage ("Hello, World!")

At this point, you've seen enough Python syntax to start experimenting in IDLE with the different numerical operators and seeing what outcomes are produced. Now let's get your first program written!

The historical rite of passage for all new to programming is the "Hello, World!" program; a simple program that when executed prints the output "Hello, World!". To write this, we'll use IDLE so you can have that experience writing programs in it; in future posts, I'll press the use of Microsoft's Visual Studio Code as I feel it to be a more robust editor for your long-term growth. Let's get started!

1. Launch IDLE.
2. Using the toolbar / Menu Bar, select "File" --> "New File".
3. Copy-paste the following snippets into your new file on the lines indicated.
   * Line 1: `def main():`  
     Line 2: `print("Hello, World!")`  
     Line 3:   
     Line 4: `if __name__ == '__main__':`  
     Line 5: `main()`
   * Note the formatting - it's important that your Lines 2 and 5 have consistent space (or the tab character) preceding the line of code. Your program this in order to run (otherwise, you'll get a message similar to `expected an indented block`). The most common choices are four spaces, the tab character, or two spaces.
4. Save your file in your preferred location with the name and file extension `hello_world.py` (.py is the extension for Python Source Code files).
5. In the toolbar / Menu Bar, select "Run" --> "Run Module".
6. The result should be the original IDLE window you opened as it restarts to run your module followed by the output `Hello, World!` blue text.

Congratulations!! You've prepared and executed your first Python script! Great job!! 🤩

Now, a lot of what I had you type will probably be foreign to you; that's okay! With this experience of how to prepare a script, we can build on it in future posts and all four of those lines of code we typed will make sense (eventually).

## 💭 Thoughts from SkyNet

As I'm writing this post, it's always a good idea to hear from our soon-to-be AI overlords; I thought it fitting to ask it about where to start programming in Python, the value of IDLE as a Python editor, and if "Hello, World!" is still a valuable first program to prepare and execute. The first question, it expanded upon way more than I expected and gave a full outline of what learning Python could look like (something that will likely take us dozens of these posts to get through). The second and third questions were answered much more in-line with what I expected (summary = Yes, IDLE is good for new programmers & Yes, "Hello, World!" is still a valuable first script for new programmers for multiple reasons).

You can read the full conversation [HERE](https://chat.openai.com/share/93c97f48-181c-4d66-b275-a165fb39e956).

## 📒 Summary/Links

### Summary

* We discussed pre-requisites for this post, such as following my prior posts on installing Microsoft Visual Studio Code and Python 3.x.
* We discussed Python IDLE and the function it can serve you as you learn how to write Python code.
* We discussed numerical operators (the fancy computer word for symbols like `+` and `*`) and gave an example of many of them.
* We prepared our first Python script, "Hello World!"`, and executed it successfully.

### Links

* [Prior Blog Post on Installing Microsoft Visual Studio Code (VS Code)](https://dakotalearns.wordpress.com/2024/03/25/installation-guide-microsoft-visual-studio-code-vs-code/)
* [Prior Blog Post on Installing Python 3.x](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-%f0%9f%90%8d/)
* [Python Documentation on IDLE](https://docs.python.org/3/library/idle.html)
* [Official Python Website](https://www.python.org/)
* [Official Visual Studio Code IDE Website](https://code.visualstudio.com/)
* [Official Jetbrains PyCharm IDE Website](https://www.jetbrains.com/pycharm/)
* [Python Documentation on Numeric Types and Operations](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
* [Full ChatGPT conversation on learning Python, use of IDLE, and "Hello, World!"](https://chat.openai.com/share/93c97f48-181c-4d66-b275-a165fb39e956)

## ✅ Conclusions

This post ended up being a lot more of a lift than I expected. While I've made two separate outlines as prep work to see where each Python lesson can go, this post went completely away from both of those outlines. I ultimately feel all three of the major points covered (IDLE, Numeric Operators, and Hello, World!) are critical first-peeks into programming with Python. In addition, this post has certainly influenced what direction future posts will go.

This post forced me to slow down. While I had been able to write some posts within a week (or even 1-2 days, such as some of the Installation Guides), this post easily took three weeks to write and could have taken more time for additional refinement. That being said, we (and specifically I, in this instance) "shouldn't let perfect be the enemy of good".

From here, I'm really excited to bring future posts to you. I see a mix of very short reads on specific explanations and longer posts like this one covering some topic(s) at length; for now, it's time to click "Publish".

Until the next time we learn (or discuss) something together, have a wonderful Monday!
