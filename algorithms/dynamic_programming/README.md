---
tags: ["Dynamic Programming"]
title: Dynamic Programming
---

Some algorithm problems can be divided into sub-problems that are the same type as the original problem. These problems are usually solved with recursion: Write a function to solve the problem, then the function calls into itself with different parameters to solve sub-problems untilt a stop condition is met.

Dynamic programming is used to solve problems with the following two properties:

1. Problem can be divided into **sub-problems** that are **duplicated**. Therefore, it can be optimized by reusing results already calculated via memoization or a bottom-up tabulation.
2. **Optimal sub-structure**: an optimal solution can be constructed from optimal solutions of its sub-problems

Some non-DP example:

- Binary search: it has sub-problems and solution can be deducted from sub-structures. However, there are no duplicates in sub-problem calculation, therefore generally BS is not considered a DP algorithm.

# Dynamic Programming vs Recursion

- Dynamic Programming is used to solve **some** recursive problems. Dynamic Programming can only be used to solve recursive problems with optimal sub-structure. An example problem that is recursive but does not have an optimal sub-structure is binary search.
- Different from recursion, Dynamic Programming can be either **bottom-up** or top-down, while while recursion is always top-down. Bottom-up dynamic programming is harder to implement because you need to figure out how to iterate through the basic starting point, and iterate your way up to your target.
- Recursion involves a series calls into itself, all these calls require construction of call stacks. Top-down dynamic programming requires call stacks too. However, bottom-up Dynamic Programming can be efficient in **space usage**. A problem may use O(n) space with recursion because of call stacks, but can use O(1) space with bottom-up dynamic programming. For example, the Fibonacci problem can be solved with O(1) space with bottom-up dynamic programming, while it requires O(n) space with top-down dynamic programming or recursion.
- In terms of **time complexity**, Dynamic Programming avoids duplicate calculations by remembering intermediate results. Top-down dynamic programming can avoid these duplicate calculations via memoization of interim results that can be reused.

In other words, recursive problems satisfying the optimal sub-structure property can be solved by dynamic programming.

# References

- [Dynamic Programming on Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming)
