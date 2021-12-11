# Day 1 Problems

- [Day 1 Problems](#day-1-problems)
  - [Problem 1 - Find GCD](#problem-1---find-gcd)
  - [Problem 2 - Detect Capital](#problem-2---detect-capital)
  - [Problem 3 - Check Palindrome](#problem-3---check-palindrome)
  - [Solutions](#solutions)

## Problem 1 - Find GCD

```text
Find GCD using Euclid's Algorithm

Steps:
1. For two integers a and b, if a>b, divide a by b and reminder is r.
2. If reminder 'r' is 0, then stop; our GCD is b.
3. Otherwise, set b to a, r to b and repeat step 1 untill r is 0.
```

## Problem 2 - Detect Capital

```text
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
```

## Problem 3 - Check Palindrome

```text
Determine whether a string is a palindrome or not.

A palindrome is a string that is read the same from front to back and back to front.
For example, noon and racecar are both palindromes.
```

## Solutions

- Problem 1: Find GCD - [Solution](1_find_gcd.py)
- Problem 2: Detect Capital - [Solution](2_detect_capital.py)
- Problem 3: Check palindrome - [Solution](3_check_palindrome.py)
