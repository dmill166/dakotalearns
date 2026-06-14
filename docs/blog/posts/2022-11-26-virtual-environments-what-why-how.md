---
date: 2022-11-26
slug: virtual-environments-what-why-how
tags:
  - MacOS
  - pip
  - Virtual Environment
  - VS Code
  - Windows
categories:
  - Tutorials
---

# Virtual Environments - What, Why, How?

Now that the food coma has subsided, welcome back to my blog!

<!-- more -->

I've decided for the next topic to discuss virtual environments - what they are, why we [want to] use them, and how to set them up (in MacOS and Windows environments). This is a topic I've had professional and academic use-cases for multiple times in the past couple of years where I continue to Google how to do it each time (the examples are just far enough apart that I can't recall it by the next need arising). Like the awkward greeting with some family at the start of the holiday season, let's get this over with!

1. [A Virtual Environment? But I live in a real one!](https://dakotalearns.wordpress.com/2022/11/26/virtual-environments-what-why-how/#a-virtual-environment-but-i-live-in-a-real-one)
2. [A Virtual Environment? But I live in a real one! - Attempt #2](https://dakotalearns.wordpress.com/2022/11/26/virtual-environments-what-why-how/#a-virtual-environment-but-i-live-in-a-real-one-attempt-2)
3. [(Mac) Great, how do I do it?](https://dakotalearns.wordpress.com/2022/11/26/virtual-environments-what-why-how/#mac-great-how-do-i-do-it)
4. [(Windows) Great, how do I do it?](https://dakotalearns.wordpress.com/2022/11/26/virtual-environments-what-why-how/#windows-great-how-do-i-do-it)
5. [Is that it?](https://dakotalearns.wordpress.com/2022/11/26/virtual-environments-what-why-how/#is-that-it)
6. [Summary and Links:](https://dakotalearns.wordpress.com/2022/11/26/virtual-environments-what-why-how/#summary-and-links)
7. [Conclusion](https://dakotalearns.wordpress.com/2022/11/26/virtual-environments-what-why-how/#conclusion)

## A Virtual Environment? But I live in a real one!

Tossing `virtual environments` into the Google search popped up with a [RealPython article](https://realpython.com/python-virtual-environments-a-primer/) on the topic I'll reference from here.

*As a quick note, RealPython has a ton of great content and a newsletter that shows you cool tips and tricks about Python to help you in everyday situations!*

Per the RealPython article, through their article you can learn:  
*"...how to work with Python’s venv module to create and manage separate virtual environments for your Python projects. Each environment can use different versions of package dependencies and Python."*

Still stuck? Okay, so imagine you are using Python in combination with the [Python `pandas` library](https://pandas.pydata.org/) (*a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language*). Let's say you're using Python v3.7.15 in conjunction with `pandas` v.1.5.0, but because you're the thorough programmer I know you are you looked at the [Python Releases page](https://www.python.org/downloads/) to see what was new. You see Python v3.10.8 is available, so you check out the [Release Notes](https://docs.python.org/release/3.10.8/whatsnew/changelog.html#python-3-10-8-final) to see what's changed. Ah-ha! A hypothetical "FINALLY!" is exclaimed from your lips as you see [*gh-97612*](https://github.com/python/cpython/issues/97612) that was a worrisome security vulnerability for you is fixed! You rush through the upgrade for Python and pop open your latest **`pandas`** project to see... it's no longer functioning as expected. What happened?

In this hypothetical situation, your upgrade to Python v3.10.8 was an available option, but other dependencies (such as `pandas` or underlying libraries) weren't caught up to the newest Python yet. The upgrade now needs to be reverted and code re-confirmed as functioning before moving forward. Could this have been avoided? The answer is, as you guessed, yes.

## A Virtual Environment? But I live in a real one! - Attempt #2

Fast-forwarding from earlier context, we know Python has a new version available that fixes that annoying security vulnerability and can't wait to use it! But the **first step** will be to create a separate, virtual environment in order to pull code projects into and perform your basic regression and unit tests against. This isolated environment will serve as an area you can install specific versions of libraries and see if there are any existing conflicts or deflects when one piece of your "machine" (code project) is swapped out for a newer piece. This way, you can perform all the testing you need without the risk to production environments and only push when you're certain that it performs as expected (or at least to a quality-level you can accept).

## (Mac) Great, how do I do it?

I hope by this point you can see the value in virtual environments for development purposes, but the same can apply for new and/or side projects, proof-of-concept investigations, or a multitude of other cases. To get started:

1. Navigate to your desired test location. For this, I'll be using a GitHub repository on my local computer named `python-learning` and the terminal within [Visual Studio (VS) Code](https://code.visualstudio.com/).
2. Pass the `python3 -m venv venv` command via a terminal or command-line option
   * Per the [Python docs](https://docs.python.org/3/library/venv.html#creating-virtual-environments), the structure of this command is `python3 -m venv /path/to/new/virtual/environment`
   * In my case, I used `python3 -m venv /Users/dm/Documents/GitHub_Repositories/python-learning/testing_venv` to create my virtual environment within a (new) directory named `testing_venv`. *Note that I learned this long name isn't necessary and I easily could've passed `python3 -m venv testing_venv` to create a virtual environment named `testing_venv` that is located in the `python-learning` directory.*
3. Navigate to the folder containing your new virtual environment
   * In my case, I was already there so no need for navigation using `cd`
4. Activate the virtual environment with `source venv/bin/activate`
   * In my case, I used `source testing_venv/bin/activate`
5. You'll know if your command was successful if your command-line prompt now leads with the virtual environment name.
   * In my case, it reads as `(testing_venv) dm@Dakotas-MacBook-Pro python-learning %`

## (Windows) Great, how do I do it?

Learner's Note: I was unable to proceed with these steps without some major troubleshooting. It appeared Python was not part of my Windows PATH, so it had to be added. In addition, `python.exe` had to be disabled from app alias'. Finally, the PowerShell Execution Policy required modification to allow script calls (such as that for activating a virtual environment) To do these tasks:

1. Search in "Start" for "Edit the system environment variables"; launch this.
2. In the pop-up window, select "Environment Variables..." from the bottom right corner.
3. In the top section ("User variables"), left-click on "Path" and select "New..."
4. Launch your Windows Command Prompt/Terminal
5. Pass the command `where.exe python` to locate your Python installation. Copy the result beginning at `C:\` and through the ending `python.exe`
6. Return to the "New User Variable" window and enter "Python" as the name. Paste the previously copied path as the "value" and click "OK"
7. In the bottom section ("System variables"), left-click on "Path" and select "New..."
8. Enter "Python" as the name. Paste the previously copied path as the "value" and click "OK"
9. Restart your system and log back in as the desired user
10. Search and launch "Manage app execution aliases" from the Windows search
11. Disable the option for "App Installer - python.exe" **only** (do **NOT** disable the option for "App Installer - python3.exe")
12. Launch PowerShell as an administrator
13. Pass the command `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
14. When prompted, pass `Y` to accept the change

To get started:

1. Navigate to your desired test location. For this, I'll be using a GitHub repository on my local computer named `python-learning` and the terminal within [Visual Studio (VS) Code](https://code.visualstudio.com/).
2. Pass the `python -m venv venv` command via a terminal or command-line option
   * Per the [Python docs](https://docs.python.org/3/library/venv.html#creating-virtual-environments), the structure of this command is `python -m venv /path/to/new/virtual/environment`
   * In my case, I used `python -m venv testing_venv`**\_win**
   * NOTE: If Python is not in your PATH and you did not follow the above Learner's Note to add it, you will need to pass the entire filepath to your python.exe file in place of `python` in the above command
3. Navigate to the folder containing your new virtual environment
   * In my case, I was already there so no need for navigation using `chdir`
4. Activate the virtual environment with `venv/Scripts/activate`
   * In my case, I used `testing_venv_win/Scripts/activate`
5. You'll know if your command was successful if your command-line prompt now leads with the virtual environment name.
   * In my case, it reads as `(testing_venv_win) PS C:/Users/Dakota/OneDrive/Documents/GitHub_Repositories/python-learning>`

## Is that it?

Congratulations! You've successfully created and activated your virtual environment. You now have an isolated location to install your libraries and perform whatever tasks you desire... right? Maybe, but it's unlikely. We haven't installed any libraries! Luckily, this part should be nothing new. In case it is:

1. Resuming from the previous section, you've activated your virtual environment.
2. Let's say you want to install the `pandas` library. We'll use **[pip](https://pypi.org/project/pip/)** to do this by passing `pip install pandas`
   * You'll see a series of messages flow as the necessary underlying libraries are installed to their latest versions as specified in the pip website linked above. If you're unsure what will be installed, search your package and inspect the results to see relevant installation and configuration information
3. Wash, rinse, and repeat as needed to install all your needed libraries for this virtual environment.

In the event that you have an outlined list of the packages you need installed with the relevant version restrictions, there is an expedited command to run through the file and install it rather than the above one-by-one approach. I refreshed myself on the command from [THIS](https://note.nkmk.me/en/python-pip-install-requirements/) article. It is `pip install -r requirements.txt`. Borrowing entirely from this linked article, a sample requirements.txt file might look like the following:

```
###### Requirements without Version Specifiers ######
nose
nose-cov
beautifulsoup4

###### Requirements with Version Specifiers ######
docopt == 0.6.1             # Version Matching. Must be version 0.6.1
keyring >= 4.1.1            # Minimum version 4.1.1
coverage != 3.5             # Version Exclusion. Anything except version 3.5
Mopidy-Dirble ~= 1.1        # Compatible release. Same as >= 1.1, == 1.*
```

## Summary and Links:

Summary:

Virtual environments are great for proof-of-concept, development, testing, and many other uses

```
#MacOS:
#To create and activate the environment:
python3 -m venv /path/to/new/virtual/environment

cd /to/folder/containing/new/virtual/environment

source your_virtual_env_name/bin/activate

#To deactivate the environment when you're done working in it:
deactivate

#To install packages one-by-one:
pip install package_name

#To install packages from an outlined requirements file
pip install -r requirements.txt
```

```
#Windows:
#To create and activate the environment:

python -m venv /path/to/new/virtual/environment
chdir /to/folder/containing/new/virtual/environment
your_virtual_env_name/Scripts/activate

#To deactivate the environment when you're done working in it:
deactivate

#To install packages one-by-one:
pip install package_name

#To install packages from an outlined requirements file
pip install -r requirements.txt
```

Links:

* [RealPython Article discussing Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
* [`pandas` library homepage](https://pandas.pydata.org/)
* [Python Releases](https://www.python.org/downloads/)
* [Python 3.10.8 Release Notes (example)](https://docs.python.org/release/3.10.8/whatsnew/changelog.html#python-3-10-8-final)
* [GitHub Issue 97618 - Shell Code Injection Bug](https://github.com/python/cpython/issues/97612)
* [Visual Studio (VS) Code homepage](https://code.visualstudio.com/)
* [Python Docs - `venv` documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
* [PyPi `pip` homepage](https://pypi.org/project/pip/)
* [`pip` and `requirements.txt` illustration](https://note.nkmk.me/en/python-pip-install-requirements/)
* [(Windows) Find location of Python to ensure it's in the PATH variable](https://stackoverflow.com/questions/647515/how-can-i-find-where-python-is-installed-on-windows#:~:text=py%20installed%20location%20is%20C,if%20installed%20for%20all%20users.)
* [(Windows) `Python was not found; run the arguments...` error in VS Code](https://stackoverflow.com/questions/65348890/python-was-not-found-run-without-arguments-to-install-from-the-microsoft-store)
* [(Windows) Modify PowerShell Execution Policy](https://stackoverflow.com/questions/63012346/how-to-activate-virtual-environment-in-vscode-when-running-scripts-are-disabled)

## Conclusion

All in all, I am happy with the investigation done to refresh myself on virtual environments. The outputs include a nice summary of commands to easily perform this task in the future on either MacOS or Windows machines. I must note that the Windows configuration required much more effort on my part than the MacOS steps (seen by the additional three links at the end for Windows-only troubleshooting).

As I was writing this post, one additional thought occurred - what if we need a specific version of Python (rather than what's installed on the machine)? An excellent question for another post at another time.

Thanks for taking the time to read this post. Until the next time we learn something together, have a wonderful Saturday!
