---
date: 2023-04-03
slug: installation-guide-for-python-macos-windows
tags:
  - Blog post
  - Chat GPT
  - Chat-GPT
  - chatGPT
  - How to
  - how-to
  - IDLE
  - install
  - install-guide
  - installation
  - PATH
  - py
  - py3
  - TIOBE
categories:
  - Tutorials
---

# Installation Guide for Python - MacOS & Windows

## Welcome back!

Why, hello there! 👋 It's been almost two months since I last blogged to you all about ERDs (Entity-Relationship Diagrams) and we walked through some foundations as well as use cases for them.

<!-- more -->

In these last two months, I've had a very busy personal life!

* 😥Learning how to navigate grief
* 🧑‍💼Navigating the job market
  + 🎉...including starting a new job as [Senior Data Analyst at DISH](https://www.linkedin.com/posts/dakota-miller-_5g-seniordataanalyst-dataanalyst-activity-7043986978287079424-M8n6?utm_source=share&utm_medium=member_desktop)!
* 🏫Navigating my [CS 6400](https://omscs.gatech.edu/cs-6400-database-systems-concepts-and-design) [OMSCS](https://omscs.gatech.edu/home) Course at Georgia Tech
* 🐕Raising our golden retriever puppy (Jackson is 10 months old now!)
* 🎖️Began volunteering with [DAMA-RMC](https://dama-rmc.wildapricot.org/) (Data Management Association - Rocky Mountain Chapter) as part of the Memberships and Partnerships Committee

Through talking with close ones as well as coworkers, I realized a common question of "Where can I learn this?" or "How do I get started with that?" as it applies to programming languages and similar technical ideas. Until I get bored of it (could be a week, could be a decade), I've decided to take on this endeavor of providing meaningful and simply-written content to help people start on their own learning journeys (be it as a hobby, a job, or anything in between). As you think of topics or subject areas you'd like more information on, navigate over to my Contact Me and drop me a line with your idea.

Enough words - let's learn how to install Python! 🐍

1. [Welcome back!](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/#welcome-back)
2. [Why a Python installation guide?](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/#why-a-python-installation-guide)
3. [Python Installation on macOS 🍎](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/#python-installation-on-macos)
4. [Python Installation on Windows 🪟](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/#python-installation-on-windows-1)
5. [To add to PATH or not - that is the question ❓](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/#to-add-to-path-or-not-that-is-the-question)
6. [ChatGPT PATH Question 🤖](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/#chatgpt-path-question)
7. [Summary and Links](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/#summary-and-links)
8. [Conclusion](https://dakotalearns.wordpress.com/2023/04/03/installation-guide-for-python-macos-windows/#conclusion)

## Why a Python installation guide?

According to the TIOBE Index for March 2023, Python remains at #1 as the most popular programming language (it also achieved this for March 2022). With it being high-level (meaning you can read and write it easily as it is similar to writing a paper), flexible (solves simple and complex problems alike), and continuing to grow (whether you need data analysis, application programming, or running a coding seminar to get children interested in programming), there doesn't seem to be any limit to me what the Python language can be used for.

My goal for you is by the end of this guide, you'll have Python installed on your machine and able to use the built in [IDLE (Integrated Development and Learning Environment)](https://docs.python.org/3/library/idle.html) to write programs. I'll put out more posts in the future suggesting other editors, but there's nothing wrong with starting in IDLE.

## Python Installation on macOS 🍎

1. Start by navigating to [python.org](https://www.python.org/). This is the official site for Python. There are other ways to obtain it, but you should follow those other methods with caution.
2. In the pane of option at the top, hover over "Downloads" and select "All releases".
3. Now that you're on the Downloads page, towards the top of the page you should see an "Active Python Releases" section. My preference is to use the latest version of Python **that is in security status** (not bugfix). At the time of writing this (2023-04-03), that appears to be Python 3.9.
4. Hover over "Downloads" again, but this time select "macOS".
5. Within the "Stable Releases" column, the latest version I see with an installer file available is `Python 3.9.13 - May 17, 2022`. Select the appropriate installer to your machine (if you have an Intel CPU, you may select the Intel-only installer; otherwise or if desired, select the universal2 installer).
6. The .pkg installer should go to your Downloads folder (in my case, it was named `python-3.9.13-macos11.pkg`). Double click the installer.
7. This should load an installer window titled "Install Python". If it does not, start Googling your experience/symptoms because something's not right.
   * Select "Continue" on the Introduction page you're presented with.
   * You should always read the "Read Me" agreement for things you install/agree to. Once you have, select "Continue".
   * You should always read the "License" agreement for things you install/agree to. Once you have, select "Continue".
     + A pop-up window will appear asking if you've read it. It's so nice it even presents an option to take you to the license to read. Once you have, select "Agree".
   * The Installation Type page should appear advising how much storage space Python will need. If standard installation is acceptable, select "Install". You can customize the installation files using "Customize", though note all my future documentation guides will assume you installed using the standard installation.
   * You may receive a pop-up window from the Installer asking to enter an administrator credential to proceed. If you agree to this or can gain those credentials being entered by an authorized admin, select "Install Software".
   * This will install Python on your machine. It may also show you the install folder as a new Finder window (titled Python 3.9). You may close this. In addition, the original install window should now be on a Summary page advising the success of your Python installation. Select "Close".

Congratulations! You've now installed Python on your machine! Stay tuned for additional posts to come about interacting with and starting to write your first Python code!

## Python Installation on Windows 🪟

1. Start by navigating to [python.org](https://www.python.org/). This is the official site for Python. There are other ways to obtain it, but you should follow those other methods with caution.
2. In the pane of option at the top, hover over "Downloads". Select "All releases".
3. Now that you're on the Downloads page, you should see towards the top an "Active Python Releases" section. My preference is to use the latest version of Python **that is in security status** (not bugfix). At the time of writing this (2023-04-03), that appears to be Python 3.9.
4. Hover over "Downloads" again, but this time select "Windows".
5. Within the "Stable Releases" column, the latest version I see with an installer file available is `Python 3.9.13 - May 17, 2022`. Select the appropriate installer to your machine (in my case, I selected `Windows installer (64-bit)`).
6. The .exe installer should go to your Downloads folder (in my case, it was named `python-3.9.13-amd64.exe`. Double click the installer.
7. This should load an installer window titled "Python 3.9.13 (64-bit) Setup" or something similar (remember, the 64-bit might change if you selected 32-bit). If this does not pop up or something else does, start Googling your experience/symptoms because something's not right.
   * Check the box at the bottom of the pop-up window for the "Add Python 3.9 to PATH". I'll explain why below.
   * Select "Install Now" on the Introduction page you're presented with (you also have the option to "Customize installation", which I encourage you to review if interested; that being said, all my future guides will assume you installed the standard installation).
   * This will install Python on your machine. The window will transition through some download screens and result in a screen headed with "Setup was successful". Select "Close".

Congratulations! You've now installed Python on your machine! Stay tuned for additional posts to come about interacting with and starting to write your first Python code!

## To add to PATH or not - that is the question ❓

What the heck is a PATH anyways? Well, I'm glad you asked! Quoting [How-ToGeek.com](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/), "The Windows System PATH tells your PC where it can find specific directories that contain executable files." In short, if you open up Command Prompt or another terminal-interface, it allows you to call applications/programs by name instead of their (sometimes, very long) actual storage destinations. Things like `ipconfig`, `ping`, or as you may see in other guides about installing Python, even `python3` are examples of being able to easily access applications by adding them to PATH.

Overall, I tend to add these to PATH. The downside you'll read online is that it can interfere if you're running multiple different versions of the application (as one might with Python). However, once you reach that level of programming, you tend to command implementation of virtual environments to solve those problems; basically, if you're a casual or hobbyist programmer, don't worry and add it to PATH. 🤓

## ChatGPT PATH Question 🤖

In case you haven't heard about ChatGPT (an AI, or artificial intelligence, chat-bot) with it's latest release, check out this post by ZDNet [here](https://www.zdnet.com/article/what-is-chatgpt-and-why-does-it-matter-heres-everything-you-need-to-know/). I thought it would be good to ask it the question about adding Python to PATH during a Windows installation to see what it's like (note, this is my first interaction with ChatGPT). I was not disappointed with [the response](https://chat.openai.com/share/6457af89-96a1-4947-8a57-ecf18162df3d).

> **My Question**
>
> "*When installing Python on Windows, I see an option to "Add to PATH"? What does this mean and should I consider selecting that option?*"
>
> [**ChatGPT's Response**](https://chat.openai.com/share/6457af89-96a1-4947-8a57-ecf18162df3d)
>
> "*Add to PATH" is an option that allows you to add Python to the PATH environment variable in Windows, which is a list of directories that the operating system searches for executable files when you type a command in the command prompt.  
>   
> Selecting this option can be helpful because it makes it easier to run Python commands from the command prompt or from other programs without having to manually specify the full path to the Python executable. If you don't select this option, you'll need to specify the full path to the Python executable every time you want to run a Python command from the command prompt or from other programs.  
>   
> Therefore, it is generally a good idea to select the "Add to PATH" option when installing Python on Windows, unless you have a specific reason not to. This option will also allow you to install Python packages and modules using pip, the Python package manager, from any directory in the command prompt.*"

## Summary and Links

Python is easy to install on MacOS, Windows, or even Linux (I may do a Linux series one day, but today is not that day). It's high-level (easier to read and write than low-level languages like assembly or machine code), flexible (can solve common household problems or enterprise solutions for the highest Fortune companies), and continues to see growth (indicated by being the #1 most popular language per the TIOBE index).

* [TIOBE Index stating Python is #1 most popular language in March 2023](https://www.tiobe.com/tiobe-index/)
* [Documentation around Python's IDLE (Integrated Development and Learning Environment)](https://docs.python.org/3/library/idle.html)
* [Official Python website](https://www.python.org/)
* [What is Chat GPT?](https://www.zdnet.com/article/what-is-chatgpt-and-why-does-it-matter-heres-everything-you-need-to-know/)
* [ChatGPT Conversation on Windows PATH](https://chat.openai.com/share/6457af89-96a1-4947-8a57-ecf18162df3d)

TL;DR Install Guide for Python:

1. Navigate to [python.org](http://python.org)
2. Download the desired version for your OS
3. Launch the installer
4. Navigate the steps (default options are fine for most first-time users)
5. Achieve success

## Conclusion

The installation of Python is a relatively easy and quick task to accomplish. If you followed these steps, you likely now have it installed and can start exploring the installation at your leisure. We navigated why to install Python, how to do it on macOS and Windows, PATH significance towards a Windows installation, and ChatGPT's response on the topic of PATH.

I'm currently playing with the idea of more Python content to follow or other installation guides (such as MySQL, SQL Server, and Visual Studio Code [this last one I'll be using for Python!]). We'll see where the dopamine leads next time I sit down to write.

Thanks for taking the time to read this post. Until the next time we learn (or discuss) something together, have a wonderful Monday!
