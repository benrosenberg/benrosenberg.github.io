---
title: CSCI 13300 SP 2025
author: "[Go to homepage](https://benrosenberg.info/teaching/sp25/csci13300.html)"
date: "Last updated: 2025-01-25"
css: ../../style.css
---

# Unit 1 Assessment

## Due date and submission

This assignment is due **February 8th** at 11:59 PM. Submit your solution on BrightSpace, under the "Unit 1" assignment.

**Please copy your code into the text box, don't submit a file. This will make it easier for me to grade.**

You can submit multiple times. I will only grade your last submission.

# Instructions

Write a program in Python that performs the following tasks:

## Task 1

Print out the unique letters contained in the word "manatee". (Don't hardcode the list of unique letters, have you program determine them on its own.)

Your program's output should start like this:

```plaintext
m
a
n
t
...
```

## Task 2

Generate all possible questions of the form "Can a *X* be *Y*?", where X is a word from the list ["goose", "dog", "cat", "rhinoceros"], and Y is a word from the list ["orange", "happy", "eloquent"]. (Your program doesn't have to *answer* the questions, it just has to print them out.)

Your program's output should start like this:

```plaintext
Can a goose be orange?
...
```

## Task 3

For each of the animals in the list in Task 2, print out which letters they have in common with "manatee".

Your program's output should start like this:

```plaintext
goose and manatee share the letter e
dog and manatee no letters
cat and manatee share the letters a and t
...
```

# Final output

Your program's final output should look something like the following:

```plaintext
m
a
n
t
e
Can a goose be orange?
Can a goose be happy?
Can a goose be eloquent?
Can a dog be orange?
Can a dog be happy?
Can a dog be eloquent?
Can a cat be orange?
Can a cat be happy?
Can a cat be eloquent?
Can a rhinoceros be orange?
Can a rhinoceros be happy?
Can a rhinoceros be eloquent?
goose and manatee share the letter e
dog and manatee share no letters
cat and manatee share the letters a and t
rhinoceros and manatee share the letters n and e
```

# Notes

You should be able to do all of the tasks with only the Python topics we covered in class so far. However, if you want to try doing the homework in a more idiomatic ("Pythonic") way, you could try the following questions in Google:

- What is the append method of lists in Python?
- How does the format method of strings work in Python?
- How does the join method of strings work in Python?

The Python documentation may also be helpful: [Python 3.10 documentation](https://docs.python.org/3.10/)