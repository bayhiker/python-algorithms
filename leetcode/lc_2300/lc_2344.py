class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        return self.min_operations(nums, numsDivide)

    def min_operations(self, nums: list[int], nums_divide: list[int]) -> int:
        from functools import reduce
        from math import gcd

        greatest_common_divisor = reduce(gcd, nums_divide)
        nums.sort()
        for i in range(len(nums)):
            if greatest_common_divisor % nums[i] == 0:
                return i

        return -1
