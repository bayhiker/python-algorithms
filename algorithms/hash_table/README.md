---
tags: ["Hash Table", "Hash", "Hash Map"]
title: Hash Table
---

A hash table, or hash map, is a data structure `h` containing <key, value> pairs. In absence of key conflicts, given a key `k`, h[k] can be retrieved in time O(1). On average, hash tables are more efficient than search trees for locating values.

# Hash Table Operations

- **search**: O(1) when there is no key conflict
- **insert**: O(1) amortized for some hash functions
- **delete**: O(1) amortized for some hash functions

# Hash Function

Hash function maps a key directly to its address in the hash table.

Requirements of hash functions:

- Uniform distribution, to reduce collision possibility
- Avoid clustering to improve lookup efficiency

Frequently used hashing functions:

- modular hashing: h(k) k % m, for some m. m is usually the number of buckets
- multiplicative hashing: multiply k by a very large number: h(k) = floor(m * frac(k*a)), where k is the integer key, a is a real number, frac() gets the fractional part of a real number, and floor returns the next smallest integer. This is more prone to clustering.
- Cyclic redundancy checks (CRC): Suitable for longer stream of data, h(k) = CRC(stream-of-data-so-far)
- Cryptographic hash functions: make it computationally infeasible to get key from hash.
- Pre-compiled hash, if keys are available beforehand.

# References

- https://www.cs.cornell.edu/courses/cs3110/2008fa/lectures/lec21.html
