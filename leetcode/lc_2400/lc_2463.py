class Solution:
    # TODO TLE
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        return self.minimum_total_distance(robot, factory)

    def minimum_total_distance(self, robot: list[int], factory: list[list[int]]) -> int:
        # len(robot) = m, len(factory) = n
        # dp[i][j][k]: Fix i'th robot in factory j which already fixed k robots
        # dp[m][j][k] = 0
        # dp[i][n][k] = inf
        m, n = len(robot), len(factory)
        robot.sort()
        factory.sort()

        from functools import lru_cache

        @lru_cache
        def dp(i, j, k):
            if i == m:
                return 0
            if j == n:
                return float("inf")
            skip_factory = dp(i, j + 1, 0)
            use_factory = (
                dp(i + 1, j, k + 1) + abs(robot[i] - factory[j][0])
                if k < factory[j][1]
                else float("inf")
            )
            return min(skip_factory, use_factory)

        return dp(0, 0, 0)
