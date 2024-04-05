class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        return self.min_increment_for_unique(nums)

    def min_increment_for_unique(self, nums: list[int]) -> int:
        # Sort nums, and put them into where they should be one by one
        # smaller/earlier numbers are always seated first, even if that means
        # taking the place of a larger/later number
        nums.sort()
        move_to, min_incs = 0, 0
        for i, num in enumerate(nums):
            move_to = max(num, move_to)
            min_incs += move_to - num
            move_to += 1
        return min_incs
