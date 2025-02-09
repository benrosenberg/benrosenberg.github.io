---
title: CSCI 13300 SP 2025
author: "[Go to homepage](https://benrosenberg.info/teaching/sp25/csci13300.html)"
date: "Last updated: 2025-02-09"
css: ../../style.css
---

# Unit 2 Assessment

## Due date and submission

This assignment is due **February 15th** at 11:59 PM. Submit your solution on BrightSpace, under the "Unit 2" assignment.

**Please copy your code into the text box, don't submit a file. This will make it easier for me to grade.**

You can submit multiple times. I will only grade your last submission.

## Data

This assignment uses the file [julius_caesar.txt](julius_caesar.txt). You can click on the filename to download the file. If it opens in your browser, can you use the shortcut `Ctrl + S` (or `Cmd + S` on macOS) to save the file to your computer.

**Note: Before February 9th at around 2 PM, the above file had issues and was not possible to read without specifying the UTF-8 encoding. I have fixed the file so it should now be possible to read it without running into issues.** Let me know if you have any issues. If you downloaded the file before the fix, please re-download it.

# Instructions

Write a program in Python that performs the following tasks:

## Task 1

Read in the contents of the provided file [julius_caesar.txt](julius_caesar.txt) and print the following information about the file's contents:

1. The total number of words in the file
2. The average number of words per line (take the total number of words in the file and divide it by the number of lines in the file)
3. The line with the most words, and the number of words that this line has
4. The total number of lines in your Python source code (you should be writing this code in a `.py` file)

Your program should have the following output for this task:

```plaintext
Total number of words: 21011
Average number of words in a line: 4.525306913633426
Longest line has 17 words: Nay, I beseech you, sir, be not out with me; yet, if you be out, sir, I

Total number of lines in Python source code: 33
```

## Task 2

Use the contents of the file [julius_caesar.txt](julius_caesar.txt) that you downloaded earlier to make an interface for looking up a word in the file.

The user should be able to enter a word (in the below example, `Brutus`) and after hitting Enter, your program should print out the first (up to) 10 lines that contain that word, and the total number of lines that contain it.

The interface should look something like this:

```plaintext
Enter word: Brutus
 Scene I. Rome. Brutus’ orchard

 Scene IV. Another part of the same street, before the house of Brutus

 Scene II. Before Brutus’ tent, in the camp near Sardis

 Scene III. Within the tent of Brutus

Brutus and Cassius.

VARRO, CLITUS, CLAUDIUS, STRATO, LUCIUS, DARDANIUS, Servants to Brutus

PORTIA, wife to Brutus

Calphurnia, Portia, Decius, Cicero, Brutus, Cassius and Casca; a great

[_Sennet. Exeunt all but Brutus and Cassius._]

Brutus, I do observe you now of late:

172 lines contain Brutus
```

# Final output

Your program's final output should look something like the following (assuming the word chosen by the user is `Brutus`):

```plaintext
Total number of words: 21011
Average number of words in a line: 4.525306913633426
Longest line has 17 words: Nay, I beseech you, sir, be not out with me; yet, if you be out, sir, I

Total number of lines in Python source code: 33
Enter word: Brutus
 Scene I. Rome. Brutus’ orchard

 Scene IV. Another part of the same street, before the house of Brutus

 Scene II. Before Brutus’ tent, in the camp near Sardis
 Scene III. Within the tent of Brutus

Brutus and Cassius.

VARRO, CLITUS, CLAUDIUS, STRATO, LUCIUS, DARDANIUS, Servants to Brutus

PORTIA, wife to Brutus

Calphurnia, Portia, Decius, Cicero, Brutus, Cassius and Casca; a great

[_Sennet. Exeunt all but Brutus and Cassius._]

Brutus, I do observe you now of late:

172 lines contain Brutus
```

# Notes

You should be able to do all of the tasks with only the Python topics we covered in class so far. However, if you want to try doing the homework in a more idiomatic ("Pythonic") way, you could try the following questions in Google:

- What is list comprehension in Python?
- How does the sum function work in Python?
- How does the join method of strings work in Python?
- How does slicing work in Python?

The Python documentation may also be helpful: [Python 3.10 documentation](https://docs.python.org/3.10/)