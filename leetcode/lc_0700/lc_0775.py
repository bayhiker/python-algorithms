class Solution:
    # Local inversion is always global inversion
    # Therefore if there's a global inversion that's not local return false
    # nums[i] - i > 1
    def isIdealPermutation(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] - i > 1 or nums[i] - i < -1:
                return False
        return True
