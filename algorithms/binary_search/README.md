---
title: Binary Search
tags: ["Binary Search"]
---

Binary search is a commonly-used search method on sorted arrays/lists. If we need to find element x inside **sorted** array a, then `binary_search(a, x)` can be implemented with Python bisect library.

# The bisect module

The `bisect` module is called bisect because it uses a basic bisection algorithm: Given element x and sorted array a, the bisect methods returns an index that splits array `a` into two parts: one part no larger than `x`, the other part no smaller than `x`. There are three bisect methods in the bisect library:

- `bisect_right` (alias `bisect`): returns the location to insert `x` while keeping `a` sorted. If `x` is already in `a`, then return the location next to the last appearance of `x`.
- `bisect_left`: returns the location to insert `x` while keeping `a` sorted. If `x` is already in `a`, then return the location of the first appearance of `x`.

`bisect` module also has three other methods that inserts `x` into `a` while keeping a sorted

- `insort_right` (alias `insort`): inserts `x` into a at location `insect_right`
- `insort_left`: inserts `x` into a at location `insect_left`

# Some interesting observations of bisect methods

- `bisect` methods return insertion points: the index of `x` in a after insertion
- `bisect.bisect` is a short-hand for `bisect_right` and is always the same as `bisect_right`.
- When `a` is sorted, and `x` is not found in `a`, `bisect` is also the same as `bisect_left`

# What if `a` is not sorted or `a` is not in increasing order?

Looking at the [source code of bisect](https://github.com/python/cpython/blob/3.9/Lib/bisect.py), `bisect` implementation doesn't check if `a` is properly sorted. Therefore, the behavior of `bisect`, `bisect_left`, and `bisect_right` is not defined.
