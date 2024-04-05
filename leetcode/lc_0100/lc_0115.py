class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.num_distinct_dp_2n(s, t)

    def num_distinct_dp_2n(self, s: str, t: str) -> int:
        # dp[j]: num of distinct subsequences of s[0:i+1] which equals t[0:j+1]
        m, n = len(s), len(t)
        dp_curr: list[int] = [0 for j in range(n)]
        dp_curr[0] = 1 if s[0] == t[0] else 0
        dp_next: list[int] = [0 for j in range(n)]
        for i in range(m):
            for j in range(n):
                if i < j:
                    continue
                elif i == j:
                    dp_next[j] = 1 if s[0 : i + 1] == t[0 : j + 1] else 0
                elif s[i] == t[j]:
                    dp_next[j] = (
                        dp_curr[j - 1] + dp_curr[j] if j > 0 else dp_curr[j] + 1
                    )
                else:
                    dp_next[j] = dp_curr[j]
            # Assign dp_next to dp_curr, old dp_curr values will be overwritten
            dp_curr, dp_next = dp_next, dp_curr
        return dp_curr[n - 1]

    def num_distinct_dp_mn(self, s: str, t: str) -> int:
        # dp[i][j]: num of distinct subsequences of s[0:i+1] which equals t[0:j+1]
        m, n = len(s), len(t)
        dp: list[list[int]] = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i < j:
                    continue
                elif i == j:
                    dp[i][j] = 1 if s[0 : i + 1] == t[0 : j + 1] else 0
                elif s[i] == t[j]:
                    dp[i][j] = (
                        dp[i - 1][j - 1] + dp[i - 1][j] if j > 0 else dp[i - 1][j] + 1
                    )
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m - 1][n - 1]
