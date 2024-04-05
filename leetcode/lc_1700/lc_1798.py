class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        return self.get_maximum_consecutive_greedy_from_0(coins)

    def get_maximum_consecutive_greedy_from_0(self, coins: list[int]) -> int:
        coins.sort()
        coins.insert(0, 0)
        n = len(coins)
        curr_sum = 0
        for i in range(1, n):
            if coins[i] <= curr_sum + 1:
                curr_sum += coins[i]
        return curr_sum + 1

    def get_maximum_consecutive_greedy(self, coins: list[int]) -> int:
        # Note that this method works with any sub-array, not necessarily from 0
        coins.sort()
        coins.insert(0, 0)
        n = len(coins)
        min_sum, max_sum = 0, 0
        left, right, curr_sum = 0, 0, 0
        while right < n:
            if coins[right] <= curr_sum + 1:
                curr_sum += coins[right]
                right += 1
                if right < n:
                    continue
            # Cannot reach the next coin
            if curr_sum - left > max_sum - min_sum:
                min_sum, max_sum = left, curr_sum
            left = right + 1
            right = left
        return max_sum - min_sum + 1

    def get_maximum_consecutive_dp(self, coins: list[int]) -> int:
        # Note that this dp method works with any sub-array, not necessarily from 0
        # dp[i][j] = [x, y] coins[i:j+1] can make numbers x to y
        # dp[i][j] = merge dp[i][k] dp[k+1] if possible, for k >i and k < j- 1
        n = len(coins)
        dp: list[list[list[int]]] = [[[0, 0] for j in range(n)] for i in range(n)]
        coins.sort()
        for i in range(n):
            dp[i][i] = [0, 1] if coins[i] == 1 else [coins[i], coins[i]]
        for x in range(1, n):  # From diagonal, process layer by layer until (0, n-1)
            for i in range(n - x):
                j = i + x
                left_ij, right_ij = dp[i][j]
                for k in range(i, j):
                    left_ik, right_ik = dp[i][k]
                    left_kj, right_kj = dp[k + 1][j]
                    if left_kj + left_ik <= right_ik + 1:
                        # Can merge i thru k and k+1 thru j
                        if right_kj + right_ik - left_ik > right_ij - left_ij:
                            left_ij, right_ij = left_ik, right_ik + right_kj
                    elif left_kj + left_ik <= right_kj + 1:
                        if right_kj + right_ik - left_kj > right_ij - left_ij:
                            left_ij, right_ij = left_kj, right_ik + right_kj
                    else:
                        if right_ik - left_ik > right_ij - left_ij:
                            left_ij, right_ij = left_ik, right_ik
                        if right_kj - left_kj > right_ij - left_ij:
                            left_ij, right_ij = left_kj, right_kj
                dp[i][j] = [left_ij, right_ij]
        return dp[0][n - 1][1] - dp[0][n - 1][0] + 1
