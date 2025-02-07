---
title: CSCI 13300 SP 2025
author: "[Go to homepage](https://benrosenberg.info/teaching/sp25/csci13300.html)"
date: "Last updated: 2025-02-06"
css: ../../style.css
---

# Unit 3 Assessment

## Due date and submission

This assignment is due **February 22nd** at 11:59 PM. Submit your solution on BrightSpace, under the "Unit 3" assignment.

**Please copy your code into the text box, don't submit a file. This will make it easier for me to grade.**

You can submit multiple times. I will only grade your last submission.

## Data

This assignment uses the file [guido_tweets.txt](guido_tweets.txt), which contains a list of tweets made by Guido van Rossum, the creator of the Python programming language. You can click on the filename to download the file. If it opens in your browser, can you use the shortcut `Ctrl + S` (or `Cmd + S` on macOS) to save the file to your computer.

# Instructions

Write a program in Python that performs the following tasks:

## Task 1

Print the following:

1. The total number of tweets in the file
2. The tweet that contains the most words

Expected output:

```plaintext
Number of tweets: 792
Tweet with max number of words: [Repeat so more people are aware of this]\\nPython 4 FAQ.\\n1. The version after 3.9 is 3.10; in fact it already exists (in github master).\\n2. If there ever is a version 4, the transition from 3 to 4 will be more like that from 1 to 2 rather than 2 to 3.
```

## Task 2

A **username** is a word that begins with the `@` symbol (e.g., `@MarkTwain`).

- Clean the data before this step: make all letters lowercase (with the string `lower()` method) and remove all punctuation except for the `@` symbol
- Compile the information on how many times different usernames are mentioned in Guido van Rossum's tweets (a concordance)
- Create an interface for users to quickly look up how many times any particular username is mentioned

Sample usage:

```plaintext
Enter username: gvanrossum
Not mentioned.
Enter username: @gvanrossum
Mentioned 15 times.
Enter username: dropbox
Not mentioned.
Enter username: @Dropbox
Not mentioned.
Enter username: Dropbox
Not mentioned.
Enter username: @dropbox
Mentioned 5 times.
```

Note that the lookup is case-sensitive, and requires the `@` symbol to be included.


# Final output

Your program's final output should look something like the following:

```plaintext
Number of tweets: 792
Tweet with max number of words: [Repeat so more people are aware of this]\\nPython 4 FAQ.\\n1. The version after 3.9 is 3.10; in fact it already exists (in github master).\\n2. If there ever is a version 4, the transition from 3 to 4 will be more like that from 1 to 2 rather than 2 to 3.

Enter username: gvanrossum
Not mentioned.
Enter username: @gvanrossum
Mentioned 15 times.
Enter username: dropbox
Not mentioned.
Enter username: @Dropbox
Not mentioned.
Enter username: Dropbox
Not mentioned.
Enter username: @dropbox
Mentioned 5 times.
```

# Notes

You should be able to do all of the tasks with only the Python topics we covered in class so far. However, if you want to try doing the homework in a more idiomatic ("Pythonic") way, you could try the following questions in Google:

- What is a `defaultdict` in Python?
- How does the `key` parameter of `max` work in Python?

The Python documentation may also be helpful: [Python 3.10 documentation](https://docs.python.org/3.10/)