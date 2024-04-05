# Arrays, Lists, and Strings

## KMP sub-string search algorithm

The problem is to search for word w in string s. For example, we want to search for w="aaaab" in s = "aaaaaaaab".

The brute-force approach is to have two pointers i and j each pointing to s[0] and w[0]. Then we match s[0:5] by moving i and j forward one by one at the same. When mismatch between s[4] ("a") and w[4] ("b"), then we roll back i to point to s[1] and restart the comparison process. This goes on and on util s ends or until we find w in s.

The key observation by Drs. Knuth, Morris, and Pratt was: there are information that can be recycled when there is a mismatch in the brute-force approach. For example, when we see the mismatch between characters "b" (w[4]) and "a" (s[4]), we already know  the previous four chars in s before s[4] are all a's. Therefore, it would be a wasted if we roll i back to s[1] because we already know s[0:4] is "aaaa" from our last round of comparison. In this case, we can let i pointer stay put, and point j to w[3]. If there's a match, move i and j forward.

To find out how to move j pointer, the KMP algorithm proposes a partial match table. Some people like to call the partial match table "next" table, but it it totally up to your personal taste. In the next table,
next[k] contains a integer indicating where to move pointer j where there is a mismatch for w[k+1].

Furthermore, if we observe how j can be moved, we can abstract next table generation algorithm into the following statement:

  next[k] is the largest k such that w[0:next[k]+1] == w[k-next[k]:k+1] where next[k] < k+1. Or in plain words, k is the length of the longest equal prefix and suffix of string w[0:k+1] as long as the prefix/suffix is not w[0:k+1] itself

For our example, the next table for "aaaab" is [0, 1, 2, 3, 0] because:
- next[0] is 0 because longest prefix/suffix that's not "a" itself is ""
- next[1] is 1 because longest prefix/suffix that's not "aa" is "a"/"a"
- next[2] is 2 with prefix/suffix "aa"/"aa"
- next[3] is 3 with prefix/suffix "aaa"/"aaa"
- next[4] is 0 with prefix/suffix ""/""

With the help of the next table, i pointer for s never has to be moved back,
we only have to move j back according to the value of next element right before our mismatch. Repeatedly moving j until there's a match or until j reach 0.

Note that, similar to s/w matching process, the generation process of next table can also reuse next information already generated. This youtube video has a nice explanation about how this is done in details: https://youtu.be/t6xa2p6fFS8?si=BSRAr1VfVK13j1jv


## collections.deque vs queue.Queue

queue.Queue is designed for communication between threads. It is thread-safe and has methods like put_nowait etc, but doesn't have operators like "in"

collections.deque, on the other hand, is designed as the queue data structure for regular algorithms. It is also thread safe because of Python global interpreter lock (GIL), however, it lacks methods like put_nowait, etc.

## sub-array, sub-string, and sub-sequence

A sub-array and a sub-string must be contiguous, while a sub-sequence does not have to be.

## Monotonic Stack

Given a list of items with values nums (histogram bars, numbers, etc), we can use a monotonic stack to find left_smaller and right_smaller of every item in the list in O(N) time, where N is the size of the item list and left_smaller and left_larger is defined as follows:

- *left_smaller*: the first item to the left that's smaller then the current item
- *right_smaller*: the first item to the right that's smaller then the current item

nums[i] is the bottom of sub list left_smaller[i]+1, .. , right_smaller[i] - 1. Then you can calculate largest rectangle in histogram (Leetcode 84, 2334)

To construct left_smaller and right_smaller with stack s *containing index of items*.

1. Append value 0 to the end of nums. This value 0 is smaller than all items in nums, and is used to clear items from the stack at the end.
2. Grab i'th item from nums,
    - if nums[i] is larger than nums[s[top]], set left_smaller[i] to top of stack, move on to i+1
    - if nums[i] is the same as top of stack, set left_smaller[i] to left_smaller[top of stack]
    - if nums[i] is smaller than top of stack, set right_smaller[top of stack] to i and repeat

For each i, (right_smaller[i] - left_smaller[i] - 1) * nums[i] is a max rectangle limited by value of nums[i].