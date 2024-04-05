class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        return self.min_falling_path_sum(matrix)

    def min_falling_path_sum(self, matrix: list[list[int]]) -> int:
        # m len(matrix), n len(matrix[0]). At row r,
        # dp[i]: if i = 1..n min falling path from matrix[r][i-1] in current row to row m - 1
        #        inf if i == 0 or n+1 (prepend and append 0 for easier calc)
        # dp_next[i]: inf if i == 0 or n+1, else matrix[i-1] + min(dp[i-1], dp[i], dp[i+1])
        pass
