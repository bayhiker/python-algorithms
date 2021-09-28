---
tags: ["Dynamic Programming"]
title: Dynamic Programming
---

Some algorithm problems can be divided into sub-problems that are the same type as the original problem. These problems are usually solved with recursion: Write a function to solve the problem, then the function calls into itself to solve sub-problems until a stop condition is met.

Dynamic programming is used to solve problems with the following two properties:

1. Problem can be divided into **sub-problems** (all recursive problems satisfy this property)
2. **Optimal sub-structure**: an optimal solution can be constructed from optimal solutions of its sub-problems

# Dynamic Programming vs Recursion

- Dynamic Programming is used to solve **some** recursive problems. Dynamic PRogramming can only be used to solve recursive problems with optimal sub-structure. An example problem that is recursive but does not have an optimal sub-structure is binary search.
- Dynamic Programming is **bottom-up** while recursion is top-down.
- Recursion involves a series calls into itself, Dynamic PRogramming is more efficient in **space usage**. A problem may use O(n) space with recursion because of call stacks, but O(1) space complexity with dynamic programming.
- In terms of **time complexity**, Dynamic Programming avoid duplicate calculations by remembering intermediate results. Recursion can also achieve this with memorization though.

In other words, recursive problems satisfying the optimal sub-structure property can be solved by dynamic programming.

# References

- [Dynamic Programming on Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming)
