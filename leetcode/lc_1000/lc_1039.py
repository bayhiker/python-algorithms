class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        """Dynamic Programming
        dp[i, j]: Min score from convex formed by vertices values[i..j]
        dp[i, j+1]: min v[i]*v[k]*v[j+1] + dp[i+1..k] + dp[k..j]
          For any vertices in [i+1..j].
          convex [i..j+1], use one of v[i+1..j] to form a triangle and separate convex into three sections.

        Base: dp[i, i+1, i+2] = v[i] * v[i+1] * v[i+2]  for 0<=i<=n-1

        Args:
            values (list[int]): _description_

        Returns:
            int: _description_
        """
        pass
