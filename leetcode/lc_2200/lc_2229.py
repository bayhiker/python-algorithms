"""
2229. Check if an Array Is Consecutive (Easy)

Given an integer array nums, return true if nums is consecutive, otherwise return false.

An array is consecutive if it contains every number in the range [x, x + n - 1] (inclusive),
where x is the minimum number in the array and n is the length of the array.
"""
# Solution: collections.Counter(): check no duplicates,
#           then check max(nums) = min(nums) + n - 1
