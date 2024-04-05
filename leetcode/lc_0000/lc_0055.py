class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # dp[i] = True nums[j] >= i - j  for any j in [0..i]
        n = len(nums)
        can_reach: list[int] = [False] * n
        can_reach[0] = True
        for i in range(n):
            if not can_reach[i]:
                next
            for j in range(nums[i]):
                if i + j == n - 1:
                    return True
                if i + j < n - 1:
                    can_reach[i + j] = True
        return False
