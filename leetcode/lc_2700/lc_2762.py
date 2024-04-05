from bisect import bisect


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        return self.continuous_subarrays_2p(nums)

    def continuous_subarrays_2p(self, nums: list[int]) -> int:
        # 2 pointers
        total, p, q, curr_window, n = 0, 0, 0, [nums[0]], len(nums)
        while True:
            if curr_window[len(curr_window) - 1] - curr_window[0] <= 2:
                # Any subarray starting from any item in curr_window and ends at nums[q] qualifies
                total += q - p + 1
                q += 1
                if q >= n:
                    break
                curr_window.insert(bisect(curr_window, nums[q]), nums[q])
            else:
                curr_window.remove(nums[p])
                p += 1
        return total

    def continuous_subarrays_n_2(self, nums: list[int]) -> int:
        # O(n**2)
        # dp[0] = 1
        # dp[i+1] = dp[i] + more possible subarrays ending at i+1
        # Return dp[0, n-1]
        n = len(nums)
        total = 1
        for i in range(1, n):
            curr_min, curr_max = nums[i], nums[i]
            for j in range(i, -1, -1):
                curr_max, curr_min = max(curr_max, nums[j]), min(curr_min, nums[j])
                if curr_max - curr_min <= 2:
                    total += 1
                else:
                    break
        return total
