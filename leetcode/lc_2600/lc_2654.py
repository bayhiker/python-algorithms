class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return self.min_operations(nums)

    def min_operations(self, nums: list[int]) -> int:
        # loop i thru n, and j from i thru n.
        # Find accumulative gcd until it reaches 1,
        # steps needed for all nums to return to 1 is j-i + (len(nums) - 1)
        # Find min for all such pairs
        pass
