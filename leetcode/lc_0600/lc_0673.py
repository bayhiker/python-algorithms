from collections import deque


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        return self.find_number_of_lis_dp(nums)

    def find_number_of_lis_dp(self, nums: list[int]) -> int:
        # dp[i] = [max_len, count], max_len and count of sub-seq of nums[0:i+1] that end with nums[i]
        n = len(nums)
        dp: list[list[int]] = [[1, 1] for i in range(n)]
        for i in range(n):
            if i == 0:
                dp[i] = [1, 1]
                continue
            for k in range(i):
                if nums[i] > nums[k]:
                    len_k = dp[k][0] + 1
                    if len_k > dp[i][0]:
                        dp[i] = [len_k, dp[k][1]]
                    elif len_k == dp[i][0]:
                        dp[i][1] += dp[k][1]
        max_len, count = 0, 0
        for l, c in dp:
            if l > max_len:
                max_len = l
                count = c
            elif l == max_len:
                count += c
        return count

    def find_number_of_lis_mono_stack(self, nums: list[int]) -> int:
        # Use monotonic queue for find LIS, note number of LISes
        # NOTE this finds max length, but not the number of LIS
        s = deque()
        max_len, result = 0, 0
        for i, num in enumerate(nums):
            if len(s) == 0 or num > nums[s[-1]]:
                s.append(i)
            else:
                while len(s) > 0 and nums[s[-1]] >= num:
                    s.pop()
                s.append(i)
            if len(s) == max_len:
                result += 1
            elif len(s) > max_len:
                max_len, result = len(s), 1
        return result
