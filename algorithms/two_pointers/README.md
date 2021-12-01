---
tags: ["Two Pointers"]
title: Two Pointers
---

Pointers are important in traversing through arrays, linked lists, matrices, and strings. The two pointer approach, as the name sounds, uses two pointers together. It may sound trivial moving from a single pointer to two pointers, however, in practice this does a lot of magic in solving computing problems.

# Varieties of two pointer techniques

There are at least two typical cases of using two pointers:

First, **opposing pointers**: p1 points to the start, p2 points to the end. Both moving towards each other. A typical example of this two pointer approach is _string reversal_: p1 points to the start of a string, p2 points to the end of the string, swap chars at p1 and p2, then move p1 and p2 until they meet.

Second, **fast-and-slow-pointers**: p1 and p2 both point to the start, p1 is slower while p2 is faster. One example of using the slow-fast-pointers technique is in the _loop detection_: To find a loop in a singly-linked list, p1 and p2 both start at the head node of a singly linked list, with p2 going twice as fast as p2. They will eventually meet each other when there is a loop. If they don't meet, then there's no loop. This is also called the Floyd's loop detection algorithm. In addition **to find the length of the loop**, let p2 stop at the meeting node, and let p1 continue moving while counting. When p1 meets p2 again, the counter is the length of the loop.

# References

- [The Two Pointers Technique](https://algodaily.com/lessons/using-the-two-pointer-technique)
