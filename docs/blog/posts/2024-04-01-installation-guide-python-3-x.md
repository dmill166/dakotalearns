---
date: 2024-04-01
slug: installation-guide-python-3-x
tags:
  - AI
  - Artificial Intelligence
  - Blog post
  - chatGPT
  - coding
  - How to
  - install
  - programming
  - py
  - Python3
  - VS Code
categories:
  - Tutorials
---

# Installation Guide: Python 3.x 🐍

Welcome back so soon after the last post!

I had a lot of fun writing the [Installation Guide for VS Code](https://dakotalearns.wordpress.com/2024/03/25/installation-guide-microsoft-visual-studio-code-vs-code/); so much, in fact, that I didn't want to wait around too much before I created the guide meant to follow it - an Installation Guide for Python 3.x!

<!-- more -->

This post, I'll dive into what Python is, why I'm choosing it, and how to install it on Windows and Mac operating systems. We'll have a guest appearance from ChatGPT and then the usual wrap-up. Without further ado, let's get started!

1. [🐍 What is Python?](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#what-is-python)
2. [⍰ Why have a series on Python?](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#why-have-a-series-on-python)
3. [📋 Installation Steps](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#installation-steps)
   1. [🪟 Windows](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#windows)
   2. [🍎 MacOS](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#macos)
   3. [🤩 Confirming Successful Installation](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#confirming-successful-installation)
4. [🤖 ChatGPT Thoughts on Python](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#chatgpt-thoughts-on-python)
5. [Summary/Links](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#summary-links)
   1. [📝 Summary](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#summary)
   2. [🔗 Links](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#links)
6. [🏁 Conclusion](https://dakotalearns.wordpress.com/2024/04/01/installation-guide-python-3-x-🐍/#conclusion)

## 🐍 What is Python?

> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.
>
> [Python Blurbs](https://www.python.org/doc/essays/blurb/)

What does all of that mean? I'm glad you asked!

* **Interpreted**. This means that Python is read by the computer one line at a time rather than translated to a low-level computer language. This makes Python less performant than other compiled languages (such as Java) with certain tasks.
* **Object-oriented**. The language is built upon the interactions with specific objects that have attributes and methods ("actions") specific to them (and especially each 'instance' of them).
* **High-level**. The Python language is closer to English than it is to low-level computer languages making it easier to read and write.
* **Dynamic typing/binding**. Variables (or 'placeholders') can have different types of objects stored in them within a short amount of time (compared to other static semantics, like Java, where an object type is rigid and can't be changed without creating a new object).
* **Scripting language**. Often used for short and automated solutions, you can quickly write a small amount of code and solve a wide range of business and personal problems.

## ⍰ Why have a series on Python?

In the companies I've worked, Python has played a valuable role regardless of sector (telecom, wholesale semiconductors/components, or IT Data Engineering). In addition, it's now popularly used across Computer Science courses. This means that I have a chance to impact individuals pursuing their academic goals, solving business problems, or interested in Python as a hobby.

In addition, the use-cases and support for Python has only exponentially grown since I was first exposed to the language 12 years ago as a junior in high school. Whether you want to make little scripts to keep your kids entertained, contribute to major OSS (open-source software), or be the hero your team at work needs, Python can fit your needs!

Let's take the next steps in your venture and get Python installed on your machine.

## 📋 Installation Steps

### 🪟 Windows

1. First, we'll download Python from the official site. Navigate to <https://www.python.org/>
2. At the top of the page, hover over the "Downloads" button to expose more options, then select "All releases"
3. I personally like to check the chart of "Active Python Releases" and download the latest version that's in 'security' status; in this case, that appears to be Python version 3.10
4. At the top of the page, hover over the "Downloads" button again to expose more options but this time select "Windows"
5. I used CTRL+F and searched "Python 3.10" to find the latest version with files available for that release; in this case, it was Python 3.10.11. From this header, select the appropriate Windows installer for your machine (most likely 'Windows installer (64-bit)')
6. Navigate to your Downloads folder and launch the .exe you just downloaded
7. In the installation window that appears, check the box at the bottom of the window that reads "Add python.exe to PATH"
8. Then, click the "Install Now" option at the top (requiring admin privileges)
9. If a pop-up window from User Account Control appears and it appears to be a legitimate message from the Python installation, click "Yes"; otherwise, click "No" (if you select "No", inspect your download for a valid checksum against the official release as notated at Python.org)
10. If you get a message after installation allowing you to "Disable PATH length limit" (requiring admin privileges), select this option, then click the "Close" button in the bottom right corner.
11. Next, launch the Microsoft Store (you'll need Python from here to be recognized in your VS Code Terminal)
12. Search "Python" in the search bar
13. From the results, find the Python version that you just downloaded (in this case, Python 3.10) - it should be a free download. Select it to open the info on that specific software
14. Select the blue "Get" button to download Python.
15. Congratulations! You've successfully installed Python on Windows!

### 🍎 MacOS

1. First, we'll download Python from the official site. Navigate to <https://www.python.org/>
2. At the top of the page, hover over the "Downloads" button to expose more options, then select "All releases"
3. I personally like to check the chart of "Active Python Releases" and download the latest version that's in 'security' status; in this case, that appears to be Python version 3.10
4. At the top of the page, hover over the "Downloads" button again to expose more options but this time select "macOS"
5. I used CMD+F and searched "Python 3.10" to find the latest version with files available for that release; in this case, it was Python 3.10.11. From this header, select the appropriate macOS installer for your machine (most likely 'macOS 64-bit universal2 installer')
6. Using Finder, navigate to your Downloads folder and open the python-3.10.11-macos11.pkg file
7. In the popup window that appears, select the "Continue" button in the bottom right corner to pass the Introduction screen
   * \*\*\*It is recommended you read all content in the Introduction screen and all following screens before making the button selections I recommend (practice due diligence)
8. Select the "Continue" button in the bottom right corner to pass the Read Me screen
9. Select the "Continue" button in the bottom right corner to pass the License screen
10. In the pop-up window that appears, click the "Agree" button (again, recommended you click "Read License" first and read/agree to all contents before continuing)
11. Select the "Install" button in the bottom right corner to pass the Installation Type" screen
    * \*\*\*If you wish to customize your installation, use the "Customize" button to the bottom left, but this is not recommended (all my subsequent guides will be based on the Standard Installation)
12. Enter your password or provide Touch ID access to enable the installation to proceed
13. Close the additional Finder window that appears showing the .pkg contents
14. In the original installation window, click the "Close" button in the bottom right corner to complete installation. You've successfully installed Python on macOS!
    * \*\*\*A pop-up window may appear offering to move the Python installer to the trash for you; select the "Move to Trash" button to complete this operation

### 🤩 Confirming Successful Installation

To ensure your installation was successful:

1. Launch the Visual Studio Code application on your machine
2. Launch the terminal window within VS Code (Windows/MacOS = CTRL + ` )
3. Type `python3` and press <Enter>
4. The result should be something similar to the following:

```
Python 3.10.11 (v3.1.11:7d4cc5aa85, Apr 4 2023, 19:05:19) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin  
Type "help", "copyright", "credits" or "license" for more information.
```

## 🤖 ChatGPT Thoughts on Python

Discussing with ChatGPT, I received similar answers to that of my own research. I asked it questions such as "What is Python? Explain like I'm 5", "What are use-cases for learning Python?" and "How do I install Python". I'll share the first answer below, but I'd encourage you to check out the conversation link to view the entire conversation. 🙂

> **Me:**
>
> What is the Python programming language? Explain it to me like I'm 5. If you include any terms that aren't common knowledge, be sure to define them or provide analogies to explain them.
>
> **ChatGPT:**
>
> Sure, I'd be happy to explain Python like you're 5 years old!
>
> Imagine you have a magic wand, and with this wand, you can make your toys do fun things. Python is like a special language that helps you talk to your computer like you talk to your toys with your magic wand. You can tell your computer what to do, like play games, draw pictures, or solve puzzles, and Python helps make it happen.
>
> Now, imagine your toys are all different and speak different languages. Some speak English, some speak Spanish, and so on. Python is like a toy language that all computers understand, no matter what language they normally speak. So when you use Python, you can make any computer do cool things, just like magic!
>
> If you want to learn more about Python and try it out yourself, you can visit the official Python website: [Python.org](https://www.python.org/).
>
> [Full ChatGPT Conversation](https://chat.openai.com/share/2a2716e8-093f-4f97-85e7-2ca465ca3f29)

## Summary/Links

### 📝 Summary

* I realized my last post on installing VS code was an absolute blast to write and decided to write another installation guide focused on Python. I start with a summary of what Python is used for, reasons I want to write a series on learning Python, and then proceed into installation guides for Python. I wrap up with the same questions posed to ChatGPT and one response + the link shared.

### 🔗 Links

* [Installation Guide for VS Code](https://dakotalearns.wordpress.com/2024/03/25/installation-guide-microsoft-visual-studio-code-vs-code/). I had so much fun writing this last post, it motivated me to write this one even sooner!
* [Python Blurbs](https://www.python.org/doc/essays/blurb/). The official Python site gave a great description of what Python is and made it easy for me to pick elements to break out and explain further for your reading.
* [Official Python website](https://www.python.org/). I reference this for where to download Python. There may be other ways (e.g., package managers), but call me old-school that I like to navigate to the trusted originator of the information.
* [Full ChatGPT Conversation](https://chat.openai.com/c/3bf931f9-c045-4101-b7ee-abcdc0ae4b52). I ask questions such as "What is Python? Explain it like I'm 5", "What are use-cases for learning Python", and "How do I install Python". ChatGPT handles it all with excellent and meaningful responses (in this case... 👀).

## 🏁 Conclusion

I started this post within four hours of publishing my last post. The energy and rush I got from writing that post was staggering and I wanted to seek it out again ASAP. Writing is currently a lot of fun and the words just seem to flow onto the digital page.

One realization I had along the way is just how many steps there were to installing Python (on both Windows and macOS). I expected macOS to have half as many steps as Windows and was mistaken. However, it was very satisfying to see the same keyboard shortcut opens the VS Code terminal across environments to validate a successful installation.

Another realization was the fact [I have previously written a Python Installation Guide blog post](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/) 😳 even more ironically, this post was nearly a year ago to the day (published April 3, 2023 whereas this post was published April 1, 2024). I feel that this guide is a more thorough step-by-step guide than my previous iteration as well as more high-level on WHY you would want to install Python to begin; however, last year's post has a great explanation of the Windows PATH variable and how that comes into play with a Windows Python installation (which I only casually cover here). This is certainly a first (writing a blog post on a topic I've previously covered exactly) and so I'll leave both posts for now.

I've already started the outline for the Learning Python series and hope to start on these posts in the coming days. I'll also be planning to include practice exercises and publish those solutions in the subsequent blog posts. For now, as the saying goes, "that's all she wrote". Until the next time we learn (or discuss) something together, have a wonderful Monday!
