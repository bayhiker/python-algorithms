"""
Sub-array with elements greater than varying threshold.

Given integer array nums, and integer threshold. Find any sub-array of sums such that every element in the sub-array is greater than threshold/k
"""


class Solution:
    def validSubarraySize(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        prev_smaller = [-1] * n
        stack = []

        nums.append(0)

        for i in range(n + 1):
            while stack and nums[stack[-1]] > nums[i]:
                index = stack.pop()
                # We know next_smaller for index'th item when it's popped
                k = i - prev_smaller[index] - 1
                if nums[index] > threshold / float(k):
                    return k
            if stack:
                # prev_smaller is set when an item is pushed in the stack
                prev_smaller[i] = stack[-1]
            stack.append(i)

        return -1
