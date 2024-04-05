class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        return self.three_sum(nums)

    def three_sum(self, nums: list[int]) -> list[list[int]]:
        # nums.sort()
        # For each nums[i], this becomes a 2sum problem for nums[i+1:] and sum of -nums[i]
        # Use 2-pointer 2sum solution, O(n**2)
        pass
