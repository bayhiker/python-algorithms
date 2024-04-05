"""
You are given an array nums consisting of positive integers.

Split the array into one or more disjoint subarrays such that:

    Each element of the array belongs to exactly one subarray, and
    The GCD of the elements of each subarray is strictly greater than 1.

Return the minimum number of subarrays that can be obtained after the split.

Note that:

    The GCD of a subarray is the largest positive integer that evenly divides all the elements of the subarray.
    A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [12,6,3,14,8]
Output: 2
Explanation: We can split the array into the subarrays: [12,6,3] and [14,8].
- The GCD of 12, 6 and 3 is 3, which is strictly greater than 1.
- The GCD of 14 and 8 is 2, which is strictly greater than 1.
It can be shown that splitting the array into one subarray will make the GC
"""


class Solution:
    def minimumSplits(self, nums: list[int]) -> int:
        # Greedy algorithm
        pass
