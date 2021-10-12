from typing import List

# lintcode_394_395_396
#
# coins in a line i:
# n coins in a line, two plays each takes one or two coins from right side,
# whoever picks the last coin wins. Given n check if first player wins the game
#
# coins in a line ii:
# There are n coins with different value in a line. Two players take turns
# to take one or two coins from left side until there are no more coins left.
# The player who take the coins with the most value wins. Given values[] check
# if first player wins can always win the game
#
# coins in a line iii:
# There are n coins in a line. Two players take turns to take a coin from one
# of the ends of the line until there are no more coins left. The player with
# the larger amount of money wins.
#

# lintcode_394
def first_wins_recursive(n: int) -> bool:
    if n <= 0:
        raise ValueError(f"Invalid n found: {n}")
    if n == 1 or n == 2 or n == 4 or n == 5:
        return True
    if n == 3:
        return False
    # first_wins_recursive(n - 2) and first_wins_recursive(n - 3):
    # If first player take one coin first, no matter second plays takes one or two coins
    # a still wins
    # first_wins_recursive(n - 3) and first_wins_recursive(n - 4):
    # If first player take two coins first, no matter second plays takes one or two coin:w
    # a still wins
    return (first_wins_recursive(n - 2) and first_wins_recursive(n - 3)) or (
        first_wins_recursive(n - 3) and first_wins_recursive(n - 4)
    )


# State transition:
# dp(n) = (dp(n-2) and dp(n-3)) or (dp(n-3) and dp(n-4))
# lintcode_394
def first_wins_dp(n: int) -> bool:
    if n <= 0:
        raise ValueError(f"Invalid n found: {n}")
    if n == 1 or n == 2 or n == 4:
        return True
    if n == 3:
        return False
    # Init with n = 5
    (n_minus_4, n_minus_3, n_minus_2, n_minus_1) = (True, True, False, True)
    for i in range(5, n):
        wins_n = (n_minus_2 and n_minus_3) or (n_minus_3 and n_minus_4)
        (n_minus_4, n_minus_3, n_minus_2, n_minus_1) = (
            n_minus_3,
            n_minus_2,
            n_minus_1,
            wins_n,
        )
    return (n_minus_2 and n_minus_3) or (n_minus_3 and n_minus_4)


# lintcode_394
def first_wins_math(n: int) -> bool:
    if n <= 0:
        raise ValueError(f"Invalid n found: {n}")
    return n % 3 != 0


# State transition
# dp[n] = min(
#     values[n] + dp[n-2], # first player takes one coin, then second player takes one away
#     values[n] + dp[n-3], # first player takes one coin, then second player takes two away
#     values[n] + values[n-1] + values[n-3], # first takes two, then second takes one
#     values[n] + values[n-1] + values[n-4], # first takes two, then second takes two
# )
# min() is used assuming second player is logical and also wants to win
# linecode_395
def first_wins_with_values_dp(values: List[float]):
    n = len(values)
    if n <= 0:
        raise ValueError(f"Invalid n found: {n}")
    if n == 1 or n == 2:
        return True
    if n == 3:
        return values[0] + values[1] > values[2]
    if n == 4:
        return max(values[0] + values[3], values[0] + values[1]) > sum(values) / 2
    (max_n_minus_4, max_n_minus_3, max_n_minus_2, max_n_minus_1) = (
        values[0],
        values[0] + values[1],
        values[0] + values[1],
        max(values[0] + values[3], values[0] + values[1]),
    )
    for i in range(5, n):
        max_n = min(
            values[i] + max_n_minus_2,
            values[i] + max_n_minus_3,
            values[i] + values[i - 1] + max_n_minus_3,
            values[i] + values[i - 1] + max_n_minus_4,
        )
        (max_n_minus_4, max_n_minus_3, max_n_minus_2, max_n_minus_1) = (
            max_n_minus_3,
            max_n_minus_2,
            max_n_minus_1,
            max_n,
        )
    return max_n_minus_1 > sum(values) / 2


#
# If n is even:
# As long as sum of all odd coins are not exactly equal to sum of all even coins
# first play is guaranteed to win:
# For the sake of argument, let's assume coins 0..n-2 are more than coins 1..n-1
# then first player can first choose the left-most coin 0, this forces player 2
# to pick either coin 1 or coin n-1 both belonging to the losing group. Same goes
# on and eventually player 1 wins.
#
# If n is odd, then we need to use DP with this state transition:
# dp[m][n] = max(
#     min(
#         values[m] + dp[m+2][n]), # first player take one from left, second also one from left
#         values[m] + dp[m+1][n-1]), # first player take one from left, second one from right
#     ),
#     min(
#         values[n] + dp[m+1][n-1]), # first player take one from right, second one from left
#         values[n] + dp[m][n-2]), # first player take one from right, second one from right
#     ),
# )
#
# lintcode_396
def first_wins_left_right_dp(values: List[float]):
    n = len(values)
    if n <= 0:
        raise ValueError(f"Invalid n found: {n}")
    if n % 2 == 0:
        return sum(values[1::2]) != sum(values[::2])
    dp = [[-1 for j in range(0, n)] for i in range(0, n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = values[i]  # First player takes the only coin
            elif j - i == 1:
                # Two coins: First player takes the more expensive coin
                dp[i][j] = max(values[i], values[j])
            elif j - i == 2:
                dp[i][j] = max(values[i], values[j]) + min(values[i : j + 1])
            else:
                dp[i][j] = max(
                    min(values[i] + dp[i + 2][j], values[i] + dp[i + 1][j - 1]),
                    min(values[j] + dp[i + 1][j - 1], values[j] + dp[i][j - 2]),
                )
    return dp[0][n - 1] > sum(values) / 2
