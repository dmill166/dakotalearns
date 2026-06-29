---
date: 2023-07-03
slug: how-to-access-credentials-securely-in-python-or-not
categories:
  - Tutorials
---

# How to Access Credentials [Securely] in Python... or not?

I'm starting to feel like a broken record.... welcome back, again!

<!-- more -->

Since my last post in April, I've been busy completing my Spring 2023 Master's course at Georgia Institute of Technology, getting accustomed to and simultaneously identifying ways to be a key contributor in my (still sort of) new role as a Senior Data Analyst at Dish Wireless, supporting my wife in her pursuit of her Master's, and continuing to navigate the after (as we discussed in "[Life and Loss](https://dakotalearns.wordpress.com/2023/01/31/life-and-loss/)").

Updates since we last learned something together...

* I'm taking a break from my Master's of Computer Science program to see what else I may want to pursue. In my personal experience at Georgia Tech, I did not find the level of gratification or satisfaction with the knowledge gained that I had hoped for when I started the program. Therefore, I'd like to explore potential other degree programs, certification programs, self-study pursuits, and finally take a chance to enjoy this thing called "free time".
* My time back at Dish has kept me busy as we completed the 70% Buildout (see the official Dish press release [HERE](https://about.dish.com/2023-06-15-The-DISH-5G-Network-is-Now-Available-to-Over-70-Percent-of-the-U-S-Population)). It's been a wild ride already leaving me excited for what the future may hold in this current career journey.
* I've been re-reading a book from my Senior Experience course with Dr. Steve Beaty at MSU Denver (CS 4360 - Technical Software Project) titled "Deep Work: Rules for Focused Success in a Distracted World" by Cal Newport. If you want to read a perspective respecting your focus in this world of distractions, I'd highly recommend it (you can find it [HERE](https://amzn.to/4uZzoAI) on Amazon — an affiliate link; [here's why](/disclaimers/#affiliate-links)).

I'll digress on me and give you what you came for - my time learning about accessing credentials in Python, various methods of accessing said credentials, and pros/cons of each approach to this problem. We'll conclude with ChatGPT's thoughts on the topic and the usual review of how writing this post went.

1. [🕵️ Investigate Security](https://dakotalearns.wordpress.com/2023/07/02/how-to-access-credentials-securely-in-python-or-not/#investigate-security)
2. [🗒️ Methods Review](https://dakotalearns.wordpress.com/2023/07/02/how-to-access-credentials-securely-in-python-or-not/#methods-review)
   1. [🚩 Python Configuration Files](https://dakotalearns.wordpress.com/2023/07/02/how-to-access-credentials-securely-in-python-or-not/#python-configuration-files)
   2. [😵‍💫 Others](https://dakotalearns.wordpress.com/2023/07/02/how-to-access-credentials-securely-in-python-or-not/#lorem-ipsum-1)
   3. [🛡️ Defense-by-depth and 🤖 ChatGPT Thoughts on Security in Python](https://dakotalearns.wordpress.com/2023/07/02/how-to-access-credentials-securely-in-python-or-not/#defense-by-depth-and-chatgpt-thoughts-on-security-in-python)
3. [📖 Summary and Links](https://dakotalearns.wordpress.com/2023/07/02/how-to-access-credentials-securely-in-python-or-not/#summary-and-links)
4. [🏁 Conclusion](https://dakotalearns.wordpress.com/2023/07/02/how-to-access-credentials-securely-in-python-or-not/#conclusion)

# 🕵️ Investigate Security

I began my investigation as I do most queries - on Google. Searching "Methods of accessing credentials in Python", the first article that came up wasn't one I was expecting - rather than Real Python, Python docs, or a company-sponsored page, I was met with YABP (Yet-Another-Blog-Post, for my YAML fans out there).

Posting at the start of 2022 on this topic, Nikolai Janakiev (Freelance Data Scientist and Data Engineer) gives a well-written post on the topic ([Working with Credentials and Configurations in Python](https://janakiev.com/blog/python-credentials-and-configuration/)); succinct with just enough detail to understand the topic and form an opinion moving forward. I'll borrow his methods & expand upon them below from my own research.

# 🗒️ Methods Review

EDIT: Defense-by-depth was added later, but takes the spotlight of this article. You can jump there [now](#defense-by-depth) or read on for all the post content.

We need to start this conversation with the question.... why? Why have a method of accessing credentials in Python aside from hard-coding them in each program we write? While reading the TowardsDataScience article on the topic, I came across a quote they reference from "The Twelve-Factor App" that answered this well:

> "*A litmus test for whether an app has all config correctly factored out of the code is whether the codebase could be made open source at any moment, without compromising any credentials. Note that this definition of “config” does not include internal application config, such as config/routes.rb in Rails, or how [code modules are connected](http://docs.spring.io/spring/docs/current/spring-framework-reference/html/beans.html) in [Spring](http://spring.io/). This type of config does not vary between deploys, and so is best done in the code.*"
>
> [The Twelve-Factor App](https://12factor.net/)

## 🚩 Python Configuration Files

Researching this topic seems to break down even further into two subdivisions: a config.py file which stores the credentials in variables that can then be imported versus use of the ConfigParser library which allows more separation of the variables with more granular controls, albeit more overhead (often separated into a .ini file). Regardless of which you choose, per [TowardsDataScience](https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3), it should 1) be easy to read and edit, 2) allow comments, and 3) be easy to deploy.

The pros of this approach include, when used in a Python-heavy/entire stack, it's natural to the developer(s) maintaining this & easy to write this into a .gitignore file to ensure it isn't committed to source code.

The cons of this approach include the ease of accidentally pushing your config.py file to a repository with other .py files (which can be forever disastrous afterwards.... see more [HERE](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)).

A config.py file could look like this:

```
#config.py
db_host = '01.01.01.01'
db_user = 'a_clever_username'
db_pass = 'a_more_clever_password'

#the_program.py
import config

local_pass = config.db_pass
#proceed to use the password you've imported
```

Use of the ConfigParser could look like this (thanks, [Xiaoxu, Python Developer & Data Engineer](http://linkedin.com/in/xiaoxugao/)):

<https://gist.github.com/highsmallxu/f028f821b88de47461a20bec1872f49f.js>

## 😵‍💫 Others

Some other methods I came across include Environment Variables, Python Dotenv, JSON (JavaScript Object Notation), and YAML (Yet Another Markup Language). Considering my learning of defense-by-depth, I'll leave these here for your awareness as I dive into more in the next section.

The big takeaway of Environment Variables, a simple key-value config.py file, or the ConfigParser Library is:

* Opting for ease of maintenance over security. All of these methods are reading from another source to determine the credential (ConfigParser able to read from multiple types such as CSV, XML, YAML, JSON, ...). That's all it comes down to (from my current understanding). The only security in place is access to where the files are stored (which is also threatened by accidental pushes to repositories).

## 🛡️ Defense-by-depth and 🤖 ChatGPT Thoughts on Security in Python

As you know from a couple of my posts, I always like to use available tools to learn more; this includes ChatGPT. I leveraged it throughout this post to research various programming techniques and security concepts, gathering vast amounts of information in a minimal amount of time. Areas I felt were unclear or inaccurate, I could press the model to consider its previous input and either defend it or revise it in light of my perspective(s).

After hours of thinking on this topic and researching it further, I think the simplest method to implement that will maximize security is defense-by-depth. What is this? I'm glad you asked.

Defense-by-depth is a lot like Swiss cheese. If you pick a single slice of cheese, you'll often have holes by which you could reach a finger or a pencil through. But if you take multiple slices and stack them on one another, you're more and more likely to get caught by a piece of cheese within the stack, unable to travel all the way through.

Defense-by-depth implements multiple security layers in order to provide a similar level of defense against unauthorized access. From a cost perspective, I think this can be implemented for free/cheap by leveraging three tools:

1. Store a [Vault by Hashicorp](https://www.vaultproject.io/) token as an environment variable
2. Use Python os.getenv() to [read that environment variable](https://www.geeksforgeeks.org/access-environment-variable-values-in-python/) and access a password stored in Vault (ideally with a user or service principal granted the least amount of access required)
3. Use this password obtained from Vault to read from a [PasswordSafe](https://pwsafe.org/) .psafe3 file.

Now, I wouldn't be a very good teacher if I didn't give you the tools to see how I came to these suggestions/conclusions. You can [view my conversation with ChatGPT here](https://chat.openai.com/share/2f739b44-3b1b-41c0-8dbb-fca6b161e8b0) and see the discussion of various methods of accessing credentials within Python as well as a question on defense-by-depth at the end.

# 📖 Summary and Links

Summary:

* There are multiple methods for accessing credentials (key-value pairs) for use in a Python Script. To name a few:
  + Key-Value File (config.py)
  + ConfigParser Library
  + Environment Variables
  + Command-line arguments
  + Key management systems
  + Secure vaults or secret management tools
* Key-Value Files are much easier to implement than secure vaults, but also offer much less security. Consider all aspects using a thorough security assessment before implementing any one (or combination) of methods
  + This could be considering the users or groups that will be accessing, how/where/when they'll be accessing, what they need access to, how often credentials are rotated/ credential complexity guidelines, logging of process/application output, .... the list goes on
* On that note, combinations of these methods can offer defense-by-depth (Swiss cheese). You could read a Vault token as an environment variable to access a secure vault password stored in Vault, then access that encrypted vault password using the Vault credential you obtain (as one example)

Links:

* [My last post, Life and Loss](https://dakotalearns.wordpress.com/2023/01/31/life-and-loss/)
* [Dish Network achieving 70% 5G Wireless Buildout FCC Milestone](https://about.dish.com/2023-06-15-The-DISH-5G-Network-is-Now-Available-to-Over-70-Percent-of-the-U-S-Population)
* [Amazon: "Deep Work: Rules for Focused Success in a Distracted World" by Cal Newport](https://amzn.to/4uZzoAI)
* [Nikolai Janakiev (Freelance Data Scientist and Data Engineer) perspective on credentials/configurations in Python](https://janakiev.com/blog/python-credentials-and-configuration/)
* [TowardsDataScience post](https://towardsdatascience.com/from-novice-to-expert-how-to-write-a-configuration-file-in-python-273e171a8eb3) on LOREM IPSUM
* [The Twelve-Factor App](https://12factor.net/)
* [Removing Sensitive data from a GitHub repo](http://Removing sensitive data from a repository - GitHub Docs(opens in a new tab))
* [Xiaoxu's Illustration of ConfigParser](https://gist.github.com/highsmallxu/f028f821b88de47461a20bec1872f49f#file-configparser_example-py)
* [Vault by Hashicorp, a KMS (Key Management System)](http://Vault by HashiCorp(opens in a new tab))
* [GeeksForGeeks explaining Environment Variables & illustrating reading them](https://www.geeksforgeeks.org/access-environment-variable-values-in-python/)
* [PasswordSafe, a secure vault/secret management tool](https://pwsafe.org/)
* [ChatGPT, conversation of Python Credential Access Methods & a very brief overview of the defense-by-depth security strategy](https://chat.openai.com/share/2f739b44-3b1b-41c0-8dbb-fca6b161e8b0)

# 🏁 Conclusion

I started on this post around three weeks ago and was about to publish it with a simple overview of the six methods I detail earlier. However, I had a thought I couldn't shake that there was more to this question and the solution that I wanted to grasp; therefore, there was more research to be done and the post to be edited before I share it with all of you.

After discovering the idea of defense-by-depth and a sample of how that looks (Environment Variables --> Vault by Hashicorp --> PWSafe, as one example), I'm happy I didn't publish it right away and continued to look deeper under the covers.

This post has made me think about security a little differently and given me some thoughts for future blog posts:

1. A practical demonstration of how to set up a simple defense-by-depth strategy for accessing credentials in Python
2. Additional interest in the blog post I'm planning for logging in Python. This research yielded to me how the logs themselves can offer a threat pending what is written while accessing credentials and environments; I'd like to learn more about this
3. The use of ChatGPT for generating code (similar to [Zach Wilson](https://www.linkedin.com/in/eczachly?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABPHqmcB2FuAuIzZ2LerHRr3Hlr7tUL8-e8&lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3B8rUskz0fS1C4MoRG3XkJWw%3D%3D)'s post today on LinkedIn about [using GPT-4 to generate code](https://www.linkedin.com/posts/eczachly_dataengineering-softwareengineering-activity-7081317225869017088-03VA?utm_source=share&utm_medium=member_desktop))
4. An investigation into the value of a business degree after obtaining a CS degree

Thanks for taking the time to read this post. Until the next time we learn (or discuss) something together, have a wonderful Monday!
