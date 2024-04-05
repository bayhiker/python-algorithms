from functools import lru_cache


class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        return self.count_partitions_dp(nums, k)

    def count_partitions_dp(self, nums: list[int], k: int) -> int:
        # https://github.com/doocs/leetcode/blob/main/solution/2500-2599/2518.Number%20of%20Great%20Partitions/README.md
        if sum(nums) < k * 2:
            return 0
        mod = 10**9 + 7
        n = len(nums)
        f = [[0] * k for _ in range(n + 1)]
        f[0][0] = 1
        ans = 1
        for i in range(1, n + 1):
            ans = ans * 2 % mod
            for j in range(k):
                f[i][j] = f[i - 1][j]
                if j >= nums[i - 1]:
                    f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % mod
        return (ans - sum(f[-1]) * 2 + mod) % mod

    @lru_cache
    def count_partitions_recursive(self, nums: list[int], k: int) -> int:
        # TODO debug
        n = len(nums)
        if n <= 1:
            # K >= 1 per constraint, so neither of the two subsets is between k and s-k]
            return 0
        s = sum(nums)
        if k > s // 2:
            return 0
        min_sum, max_sum = k, s - k
        return (
            self.count_partitions(nums[0 : n - 1], k)
            + self.count_partitions(nums[0 : n - 1], k - nums[n - 1])
        ) % (10**9 + 7)
