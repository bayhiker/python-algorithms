# leetcode_877_1140_1406_1510_1563_1686_1690_1872_2029

# Stone Game i:
# Given a row of piles of stones, each pile contains piles[i] stones.
# Alice and Bob take turns taking a pile of stones from either end.
# Alice goes first. At the end of the game, whoever gets the most
# stones wins the game.
#
# Assumptions:
# - 2 < len(piles) < 500
# - len(piles) is even
# - sum(piles) is odd, so no ties
# - Both players are logical and smart
#


from typing import List, Set
import sys
import math


# leetcode_877
def wins_stone_game_i(piles):
    return True


# Stone Game ii:
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
# On each player's turn, that player can take all the stones in the first
# X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
# The game continues until all the stones have been taken.
# Find the max number of stones Alice can get
#
# Assumptions:
# - 1 <= piles[i] <= 10000
# - 1 <= len(piles) <= 100
#
# DP state transition:
# dp[i][m] = max(sum(piles[i:]) - dp[i+k][max(m, k)]) for 1 <= k <= 2*m and i+k<=n
# When we are at dp[i][m], we should have dp[i+1..n][0..n] already filled out.
# All piles starting from i, dp[i+k][max(m,k)] is the most Bob can get when Alice
# takes k piles (i to i+k-1),
# leetcode_1140
def stone_game_ii_dp(piles):
    n = len(piles)
    dp: List[List[int]] = [[0 for m in range(0, n)] for i in range(0, n)]
    sums_from_i = piles[n - 1]
    for m in range(0, n):
        dp[n - 1][m] = piles[n - 1]
    for i in range(n - 2, -1, -1):
        sums_from_i += piles[i]
        for m in range(1, n):
            for k in range(1, 2 * m + 1):
                if i + k <= n:
                    current_max = (
                        sums_from_i - dp[i + k][max(k, m)] if i + k < n else sums_from_i
                    )  # i+k == n means Alice taking every pile from i to n-1
                    if current_max > dp[i][m]:
                        dp[i][m] = current_max
    return dp[0][1]


# Stone Game iii
# Alice and Bob plays stone game with n stones in a row. There's an integer
# on each stone. Each player can only take the first 1,2,or 3 stones.
# A player's score is the sum of the integers on all the player's stones.
# Return name of the winner, or "Tie" if nobody wins
#
# Assumptions
# - 1 <= len(values) <= 50000
# - -1000 <= values[i] <= 1000
#
# State Transition:
# dp[i] = sums[i:] - min(dp[i+1], dp[i+2], dp[i+3])
# Alice picks k stones starting from stone i (k = 1, 2, or 3)
# dp[i] is max(sums[i:] - dp[i+k]) k=1,2,3, which is sums[i:] - min(...)
#
# leetcode_1406
def stone_game_iii_dp(values: List[int]):
    n = len(values)
    dp: List[int] = [0 for i in range(0, n + 1)]
    dp[n] = 0  # dp[n] is 0 and is needed to calculate when i+k == n, to check case
    # when Alice takes all remaining values
    sum_from_i = 0
    for i in range(n - 1, -1, -1):
        sum_from_i += values[i]
        dp[i] = sum_from_i - dp[i + 1]
        for k in range(2, 4):
            if i + k <= n:
                current_max = sum_from_i - dp[i + k]
                if current_max > dp[i]:
                    dp[i] = current_max
    return (
        "Alice"
        if dp[0] > sum_from_i / 2
        else "Bob"
        if dp[0] < sum_from_i / 2
        else "Tie"
    )


# Stone Game iv
# Alice and Bob plays a game with n stones, Alice goes first.
# On each turn, a player removes a none-0 square number of stones.
# A player loses if he/she cannot make a move.
# Check if Alice wins the game
#
# Constraints:
# 1 <= n <= 10**5
#
# State Transition:
# dp[i] = or(not dp[i+k**2]) for 1 <= k and k**2 + i <= n
# dp[n] = False
#
# leetcode_1510
def stone_game_iv_dp(n: int) -> bool:
    # If n is perfect square, then Alice wins
    if int(math.sqrt(n)) ** 2 == n:
        return True
    dp = [False for i in range(0, n + 1)]
    dp[n] = False
    for i in range(n, -1, -1):
        for k in range(1, int(math.sqrt(n)) + 2):
            if i + k ** 2 <= n and not dp[i + k ** 2]:
                dp[i] = True
                break
    return dp[0]


# Stone Game v
# A row of stones with value stoneValue[]. Alice cuts the row into two
# non-empty rows. Bob throws away the row with larger value and adds
# the value of the row with smaller value. If the two portions have te
# same value, then Alice gets to decide which one to keep. Game goes on
# until there's only one stone left. Return Alice's max score
#
# Constraints:
# - 1 <= len(stoneValue) <= 500
# - 1 <= stoneValues[i] <= 10**6
#
# State transition:
# dp[i][j] = max(
#                if sum[i:k] < sum[k+1:j] then sum[i:k] + dp[i][k]
#                if sum[i:k] == sum[k+1:j] then sum[k+1:j] + dp[k+1][j]
#                if sum[i:k] == sum[K+1:j] then max of the above two scores
#            ) for i <= k <= j
# Note that this O(n**3) state transition could be slow when n approaches
# 500. Two ways to speed up:
# - Get rid of the k loop, reducing state transition to O(n**2)
# - Use recursion with memoization. This is faster than the above
#   tabulation DP approach because it avoids a lot of unnecessary
#   state transitions.
#
# leetcode_1563
#
def stone_game_v_dp(stoneValues: List[int]):
    n = len(stoneValues)
    dp: List[List[int]] = [[0 for i in range(0, n)] for j in range(0, n)]
    prefix_sums = [0]  # sum(stoneValues[i:j]) == prefix_sums(j) - prefix_sums(i)
    current_total = 0
    for stoneValue in stoneValues:
        current_total += stoneValue
        prefix_sums.append(current_total)
    for i in range(n - 1, -1, -1):
        dp[i][i] = 0  # Only one stone, game over, score 0
        for j in range(i + 1, n):
            for k in range(i, j):
                sum_i_k = prefix_sums[k + 1] - prefix_sums[i]
                sum_k_j = prefix_sums[j + 1] - prefix_sums[k + 1]
                current_max = 0
                if sum_i_k < sum_k_j and sum_i_k + dp[i][k] > dp[i][j]:
                    current_max = sum_i_k + dp[i][k]
                if sum_i_k > sum_k_j and sum_k_j + dp[k + 1][j] > dp[i][j]:
                    current_max = sum_k_j + dp[k + 1][j]
                if sum_i_k == sum_k_j:
                    current_max = max(sum_i_k + dp[i][k], sum_k_j + dp[k + 1][j])
                if current_max > dp[i][j]:
                    dp[i][j] = current_max
    return dp[0][n - 1]


# Stone Game vi
#
# Alice and Bob take turns picking out any one stone from a pile of stones.
# Each stone i has different values to Alice and Bob: aliceValues[i] vs bobValues[i].
# Return 1 if Alice can get more points than Bob, 0 if they get the same points,
# -1 otherwise
#
# Constraints:
#  -  n == len(aliceValues) == len(bobValues)
#  -  1 <= n <= 105
#  -  1 <= aliceValues[i], bobValues[i] <= 100
#
# State Transition
# dp[i] = max(aliceValues[j] - bobValues[k] + dp[i ^ j ^ k])
#   where  j & i == j: j represents one of the set bits in i, Alice picks this stone
#          k & i == k and k != j: k is another set bit in i, Bob picks this stone
# Initial state: dp[2**m] = aliceValues[m] 0<=m<=n
# This is NP and is not managable when n increases to 105.
#
# Instead of DP, use greedy algorithm, sort stones by aliceValues[i] + bobValues[i],
# then both Alice and Bob pick the largest one available on his/her turn
#
# leetcode_1686
def stone_game_vi_greedy(aliceValues: List[int], bobValues: List[int]) -> int:
    n: int = len(aliceValues)
    sorted_values = sorted(
        [(i, aliceValues[i] + bobValues[i]) for i in range(n)],
        reverse=True,
        key=lambda v: v[1],
    )
    max_diff = sum(map(lambda v: aliceValues[v[0]], sorted_values[::2])) - sum(
        map(lambda v: bobValues[v[0]], sorted_values[1::2])
    )
    return 1 if max_diff > 0 else 0 if max_diff == 0 else -1


# Stone Game vii
#
# Alice goes first and pick one stone from front or end of a row of stones
# with value stones[i]. For each round, the player gets a score equal to sum
# of all remaining stones. Return the max difference between Alice and Bob's
# scores.
#
# Constraints:
#
# - n == len(stones)
# - 2 <= n <= 1000
# - 1 <= stones[i] <= 1000
#
# leetcode_1690
def stone_game_vii_dp_memoization(values: List[int]) -> int:
    n = len(values)
    dp: List[List[int]] = [[-1 for j in range(n)] for i in range(n)]

    def solve(i, j) -> None:
        if dp[i][j] >= 0:
            return dp[i][j]
        if i == j:
            dp[i][j] = 0
        elif i + 1 == j:
            dp[i][j] = max(values[i], values[j])
        else:
            score_i = min(
                values[j] + solve(i + 1, j - 1), values[i + 1] + solve(i + 2, j)
            )
            score_j = min(
                values[i] + solve(i + 1, j - 1), values[j - 1] + solve(i, j - 2)
            )
            dp[i][j] = score_i if score_i >= score_j else score_j
        return dp[i][j]

    return solve(0, n - 1)


def stone_game_vii_dp_tabulation(stones: List[int]) -> int:
    n = len(stones)
    dp: List[List[int]] = [[0 for j in range(n)] for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if i + 1 == j:
                dp[i][j] = max(stones[i], stones[j])
            else:
                dp[i][j] = max(
                    # Alice takes i
                    min(stones[j] + dp[i + 1][j - 1], stones[i + 1] + dp[i + 2][j]),
                    # Alice takes j
                    min(stones[i] + dp[i + 1][j - 1], stones[j - 1] + dp[i][j - 2]),
                )
    return dp[0][n - 1]


# Stone Game viii
#
# For each move, a player remove x stones from the row, add the sum of removed stones'
# values. The sum is added to the player's score. After this move, a stone with value
# equal to the previous sum is added to the left of the remaining stones.
# Return the max difference between Alice's and Bob's scores
#
# Constraints:
# - 2 <= len(stones) <= 105
# - -10**4 <= stones[i] <= 10**4
#
# State transition:
# dp[i] = max(dp[i+1], prefix_sum[i]-dp[i]])) stone[i] was not taken by Alice vs taken
# If stone[i] is taken by Bob, then dp[i] = dp[i+1],
# else if i is taken by Alice, then dp[i] = pre-sum[i] - dp[i+1]
#
# leetcode_1872
def stone_game_viii_dp(stones: List[int]) -> int:

    n: int = len(stones)
    for i in range(1, n):
        stones[i] = stones[i - 1] + stones[i]  # Use stones[i] to store prefix-sum
    result = stones[-1]
    for i in range(n - 2, 0, -1):
        result = max(result, stones[i] - result)
    return result


# Stone Game ix
# Each player takes any one stone from stones[0:n]. The player loses if the sum of
# all removed stones is a multiple of 3. Bob wins after the last stone is removed.
#
# Constraints:
#
# - 1 <= len(stones) <= 105
# - 1 <= stones[i] <= 104
#
# Strategy:
# stones[i], when divided by 3, the remainder can only be 0, 1, or 2
# Suppose there are x 0s, y 1s, and z 2s.
# - If y == 0 and z == 0, Alice loses instantly after picking up the first stone
# - If y == 0 and z > 0, Alice wins if and only if there are three or more 2s
#                        and odd number of 0s. They can use 0s as fillers, odd number
#                        of fillers forces Bob to pick up third 2
# - If y > 0 and z == 0, Alice wins if and only if there are three or more 1s
#                        and odd number of 0s
# - If y != 0 and z != 0, game goes on only if 112121212.. or 2212121... with one
#   or more 0 fillers in between.
#   Case of even 0s: Alice always wins by first picking 1 or 2 that appears less often
#   Case of abs(y-z) > 2: Alice always wins by picking 1 or 2 that appears more often
#   Alice can lose if and only if odd Os and number  of 1s and 2s diff by 0, 1, or 2.
#
# leetcode_2029
def stone_game_ix_counting(stones: List[int]) -> bool:  # Branch and bound
    counter: List[int] = [0, 0, 0]
    for stone in stones:
        counter[stone % 3] += 1
    even_3x = counter[0] % 2 == 0
    if counter[1] == 0:
        # Alice wins only if there are 3 or more 2s, and odd 0s
        return counter[2] > 2 and not even_3x
    elif counter[2] == 0:
        # Alice wins only if there are 3 or more 1s, and odd 0s
        return counter[1] > 2 and not even_3x
    else:
        # Neither num of 0s nor num of 1s is 0
        return even_3x or abs(counter[1] - counter[2]) > 2


def test_stone_game_ii():
    assert stone_game_ii_dp([2, 7, 9, 4, 4]) == 10


def test_stone_game_iii():
    assert stone_game_iii_dp([1]) == "Alice"
    assert stone_game_iii_dp([1, 2, 3, 7]) == "Bob"
    assert stone_game_iii_dp([1, 2, 3, -9]) == "Alice"
    assert stone_game_iii_dp([1, 2, 3, 6]) == "Tie"


def test_stone_game_iv():
    assert stone_game_iv_dp(1)
    assert not stone_game_iv_dp(2)
    assert stone_game_iv_dp(100)
    assert not stone_game_iv_dp(7)
    assert not stone_game_iv_dp(17)


def test_stone_game_v():
    assert stone_game_v_dp([6, 2, 3, 4, 5, 5]) == 18
    assert stone_game_v_dp([7, 7, 7, 7, 7, 7, 7]) == 28
    assert stone_game_v_dp([98, 77, 24, 49, 6, 12, 2, 44, 51, 96]) == 330
    # stoneValues = [776886] * 500
    # assert stone_game_v_dp(stoneValues) == 383781684


def test_stone_game_vi():
    assert stone_game_vi_greedy([1, 3], [2, 1]) == 1
    assert stone_game_vi_greedy([1, 2], [3, 1]) == 0


def test_stone_game_vii_dp_memoization():
    assert stone_game_vii_dp_memoization([5, 3]) == 5
    assert stone_game_vii_dp_memoization([5, 5, 5, 5]) == 10
    assert stone_game_vii_dp_memoization([5, 5, 5, 5, 5]) == 10
    assert stone_game_vii_dp_memoization([5, 3, 1, 4, 2]) == 6
    assert stone_game_vii_dp_memoization([7, 90, 5, 1, 100, 10, 10, 2]) == 122


def test_stone_game_vii_dp_tabulation():
    assert stone_game_vii_dp_tabulation([5, 3]) == 5
    assert stone_game_vii_dp_tabulation([5, 5, 5, 5]) == 10
    assert stone_game_vii_dp_tabulation([5, 5, 5, 5, 5]) == 10
    assert stone_game_vii_dp_tabulation([5, 3, 1, 4, 2]) == 6
    assert stone_game_vii_dp_tabulation([7, 90, 5, 1, 100, 10, 10, 2]) == 122


def test_stone_game_viii_dp():
    assert stone_game_viii_dp([2, 2]) == 4
    assert stone_game_viii_dp([-2, -2]) == -4
    assert stone_game_viii_dp([-1, 2, -3, 4, -5]) == 5


def test_stone_game_ix_counting():
    assert stone_game_ix_counting([2, 1])
    assert not stone_game_ix_counting([2])
    assert not stone_game_ix_counting([5, 1, 2, 4, 3])
    assert not stone_game_ix_counting([2, 3])
    assert stone_game_ix_counting([20, 3, 20, 17, 2, 12, 15, 17, 4])
    assert not stone_game_ix_counting([10000] * 100000)
