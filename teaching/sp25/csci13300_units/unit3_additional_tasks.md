---
title: CSCI 13300 SP 2025
author: "[Go to homepage](https://benrosenberg.info/teaching/sp25/csci13300.html)"
date: "Last updated: 2025-02-05"
css: "../../style.css"
---

# Unit 3: Additional tasks

Please finish the "Apply what you learned" section before you begin these tasks.

Solutions will be made available at the end of class, in the same page as the solutions to the "Apply what you learned" exercises.

## Task 1: Solve a quadratic

Create a function `quadsolve` that takes in the parameters `a`, `b`, and `c` of a quadratic equation $ax^2 + bx + c = 0$ and applies the quadratic formula to determine the solutions. 

- Return the solutions as a list
- Round solutions to the nearest hundredth (two decimal places)
- Ignore complex solutions
- If there are no non-complex solutions, return an empty list

Example usage:

```python
result = quadsolve(1, 4, -5)

# prints [-5, 1]
print(result)
```

## Task 2: Matrix multiplication

Write a function `mmult2` that takes in two 2 by 2 matrices $A$ and $B$ (as 1-dimensional lists of size 4) and returns $A\times B$ (also as a 1-dimensional list of size 4).

Example usage:

```python
result = mmult2([1, 2, 3, 4], [5, 6, 7, 8])

# prints [19, 22, 43, 50]
print(result)
```

### Bonus

Create a function `mmult` to perform $n$ by $n$ square matrix multiplication:

- Determine the value of $n$ depending on the length of the inputs
- Throw an error (via `raise Exception('<your text here>')` or `assert <boolean statement>`) if the inputs are not the same length or are not square numbers

Example:

```python
result = mmult([1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1])

# prints [30, 24, 18, 84, 69, 54, 138, 114, 90]
print(result)
```

## Task 3: Guessing game

### Python's `random` function

Use the following line to import the `random` function from the standard `random` library Python provides:

```python
from random import random
```

You can call the `random` function like this:

```python
x = random()
```

This will generate a random decimal number between 0 and 1, and assign the value to the variable `x`.

### Task description

Make a game where the user needs to guess a (whole) number between 0 and 100:

- Choose the number randomly using the `random` function mentioned above
- Tell the user whether the number they guessed is too low or too high
- End the game when the user gets the number right
- Tell the user how many guesses it took them

Example:

```plaintext
Enter a number: 43
Too low!
Enter a number: 67
Too low!
Enter a number: 88
Too high!
Enter a number: 71
Too low!
Enter a number: 74
Correct! It took you 5 guesses.
```

### Bonus

- Prove that the worst case scenario for the number of guesses needed, given perfect play by the user, is $\log_2 100$
- Tell the user how efficient they were based on the theoretical worst number of guesses

## Task 4: Estimate $\pi$ with `random.random()`

Recall the formulas for the area of a square and of a circle:

- The area of a square is $d^2$, where $d$ is the side length of the square
- The area of a circle is $\pi r^2$, where $r$ is the radius of the circle

Use these formulas and the `random` function described above to estimate the value of $\pi$, by estimating frequency of random points in a square falling within a circle inscribed within it.

## Task 5: Minimum moves

Write a function `minmoves` that takes two parameters - two squares in [algebraic chess notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) - and returns the minimum number of moves required for a bishop to move from the first square to the second square.

- Assume that the board is empty
- The color of the piece does not matter
- If it's impossible for the piece to move from the first square to the second (i.e., a bishop going from a light square to a dark square), return -1

Example:

```python
result1 = minmoves('a8', 'a6')
print(result1) # prints 2

result2 = minmoves('a7', 'a6')
print(result2) # prints -1
```

### Bonus

Create a similar function for knights.

Example:

```python
result1 = minmovesKnight('a8', 'a6')
print(result1) # prints 2

result2 = minmovesKnight('a7', 'a6')
print(result2) # prints 3
```