---
tags: ["Dynamic Programming"]
title: Dynamic Programming
---

Some algorithm problems can be divided into sub-problems that are the same type as the original problem. These problems are usually solved with recursion: Write a function to solve the problem, then the function calls into itself with different parameters values to solve sub-problems until stop conditions are met when a pre-defined value is returned.

The term Dynamic Programming (DP) was coined by Dr. Richard Bellman in the 1950s. DP is mainly used to solve problems with the following two properties:

1. The problem can be divided into **sub-problems** that are **duplicated**. Therefore, it can be optimized by reusing results already calculated via  memoization or a bottom-up tabulation.
2. **Optimal sub-structure**: an optimal solution can be constructed from optimal solutions of its sub-problems

Some non-DP example:

- Binary search: although binary search has sub-problems and solution can be deducted from sub-structures. However, there are no duplicates in sub-problem calculation, therefore BS is not considered a DP algorithm. It can be solved with recursion, but it is not a problem that can be solved with DP.

# DP Implementation

- Top-down **memoization**: Still uses recursion to solve the DP-eligible recursive problems, but memoizes intermediate results so their calculations are not repeated.
- Bottom-up **tabulation**: Uses iteration to solve DP-problems. First create a dependency graph for all the optimal sub-structure calculation. This graph should be a acyclic directed graph so there's no cyclic dependency. Then calculate sub-problem result from the bottom where all dependent values are known, then all the way to the top. This method is called tabulation because we first need to tabulate all intermediate results based on 

# DP vs Recursion

- **DP problems are recursive problems, but not all recursive problems are DP problems**: DP is used to solve *some* recursive problems. DP can only be used to solve recursive problems with duplicate optimal sub-structures. An example problem that is recursive but does not have a duplicate optimal sub-structure is binary search: binary search has a sub-structure that reuses the same logic to find results from left and right sub-trees, however, because the left and right sub-trees are totally different, their results cannot be reused.
- **DP solutions can be bottom-up or top-down, while recursion is always top-down**: Different from recursion, DP can be either *bottom-up* or *top-down*, while recursion is always top-down. Bottom-up dynamic programming is harder to implement because you need to first form a acyclic dependency graph, and then iterate from the starting point where all dependent values are know, then all the way up to your target.
- **Space complexity: DP solutions may have O(1) space complexity, while recursion needs at least O(n) space**: Recursion involves a series calls into itself, all these calls require construction of call stacks. Top-down dynamic programming requires call stacks too. However, bottom-up DP can be efficient in *space usage*. A problem may use O(n) space with recursion because of call stacks, but can use O(1) space with bottom-up dynamic programming. For example, the Fibonacci problem can be solved with O(1) space with bottom-up dynamic programming, while it requires O(n) space with top-down dynamic programming or recursion because of the call stacks.
- **Time complexity: DP solutions can solve some NP recursive problems in polynomial time**: DP avoids duplicate calculations by remembering intermediate results via memoization or tabulation.

# References

- [Dynamic Programming on Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Lecture by Dr. Erik Demaine@MIT Intro to Algorithms Course 6.006]()
