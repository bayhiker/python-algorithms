from itertools import accumulate


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        return self.min_moves2(nums)

    def min_moves2(self, nums: list[int]) -> int:
        # Observation: Move all numbers to median of nums
        # https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/solutions/2215732/c-3-approaches-full-explanation/
        n = len(nums)
        nums.sort()
        mid = (n - 1) // 2
        # Loose sense of median, just use the left instead of average of two for even number of items
        median = nums[mid]
        return (
            mid * median
            - sum(nums[:mid])
            + sum(nums[mid + 1 :])
            - median * (n - 1 - mid)
        )
