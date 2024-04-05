class Solution:
    def sumImbalanceNumbers(self, nums: list[int]) -> int:
        return self.sum_imbalance_numbers(nums)

    def sum_imbalance_numbers(self, nums: list[int]) -> int:
        # Set total to 0
        # Loop through every nums[i], use seen[] to track all number already seen
        # For each number in nums[i+1:], if nums[j] is in seen, then total doesn't change
        #    otherwise total += 1 - (nums[j] - 1 in seen) - (nums[j] + 1 in seen)
        # Eventually total is the result.
        # Reference: https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/solutions/3719430/python-3-9-lines-w-explanation-t-m-88-96/
        pass
