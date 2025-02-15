---
title: CSCI 13300 SP 2025
author: "[Go to homepage](https://benrosenberg.info/teaching/sp25/csci13300.html)"
date: "Last updated: 2025-02-14"
css: ../../style.css
---

# Unit 4 Assessment

## Due date and submission

This assignment is due **March 1st** at 11:59 PM. Submit your solution on BrightSpace, under the "Unit 4" assignment.

**Please copy your code into the text box, making sure to indent it properly with whitespace so that it appears the same as in IDLE or wherever you wrote the code. This will make it easier for me to grade.**

You can submit multiple times. I will only grade your last submission.

# Instructions

Write a program in Python that plays a card game with the following rules:

1. The game starts with a certain `initial` amount of dollars.
2. At each round of the game, instead of flipping a coin, the player shuffles a deck and draws **6** cards. If the drawn hand contains at least one **ace**, the player gains a dollar; otherwise, they lose a dollar.
3. The game runs until the player either runs out of money or doubles their initial amount.

To test the game, given the `initial` amount, run it 1000 times to determine how many rounds the game lasts on average, and the proportion of rounds that were won (that is, the proportion of rounds that ended due to doubling the initial amount, as opposed to losing everything).

Provide the user with an interface to enter the intial bankroll. For each entered number, the program should respond with the average duration of the game for that initial bankroll and the percentage of rounds which were won.

Expected output (the numeric results in your output may differ due to random chance):

```plaintext
Enter initial amount: 100
Average rounds: 428.61
Percent won: 0.0 %
Enter initial amount: 10
Average rounds: 41.402
Percent won: 0.7 %
Enter initial amount: 5
Average rounds: 17.294
Percent won: 6.5 %
Enter initial amount: 2
Average rounds: 3.882
Percent won: 28.3 %
Enter initial amount: 1
Average rounds: 1.0
Percent won: 37.5 %
Enter initial amount: 20
Average rounds: 85.482
Percent won: 0.0 %
```

# Notes

You should be able to do all of the tasks with only the Python topics we covered in class so far.

If you want to use more complex functionality than what we discussed in class, the Python documentation may be helpful: [Python 3.10 documentation](https://docs.python.org/3.10/)