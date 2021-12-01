from typing import List
import sys

# Cherry Pickup:
# Given an nxn grid[i][j], each cell having values 1, 0, or -1
# (1: one cherry, 0:no cherry, -1: thorn blocking your way).
# You start from (0,0) and move right or down to (n-1, n-1),
# then move left or up back to (0, 0). Return the most cherry
# you can pick along the way, or 0 if there's no such route.
#
# Constraints:
# - n == len(grid) = len(grid(i))
# - 1 <= n <= 50
# - grid[i][j] is -1, 0, or 1.
# - grid[0][0] != -1, grid[n - 1][n - 1] != -1
#
# Key observations:
# - Result is the same as total of two persons both moving right/down
# - After step k, person A and B are on the same line parallel to
#   line (0, n-1) - (n-1, 0).
#
# State transition:
#   Suppose A is at (i1,j1), B is at (i2,j2), then i1+j1 == k, i2+j2==k.
#   Therefore DP state can be uniquely represented by dp(i1, i2, k).
#   four possible next steps
#      - (i1, j1+1, i2, j2+1)  dp(i1, i2, k+1)
#        if j1+1<n and grid(i1, j1+1) != -1 and j2+1<n and grid(i2, j2+1) != -1
#      - (i1, j1+1, i2+1, j2)  dp(i1, i2+1, k+1)
#      - (i1+1, j1, i2, j2+1)  dp(i1+1, i2, k+1)
#      - (i1+1, j1, i2+1, j2)  dp(i1+1, i2+1, k+1)
#   dp[i1][i2][k] = max(dp(-,-,k+1) + new-cherries-picked-at(i1,j1)-and-(i2,j2))
#
#
# leetcode_741
def cherry_pickup_i_dp(grid: List[List[int]]) -> int:
    n = len(grid)
    dp = [
        [[-sys.maxsize for k in range(2 * n - 1)] for j in range(n)] for i in range(n)
    ]
    dp[n - 1][n - 1][2 * n - 2] = grid[n - 1][n - 1]
    for k in range(2 * n - 3, -1, -1):
        for i1 in range(n - 1, -1, -1):
            for i2 in range(i1, -1, -1):
                # i1 and i2 are symmetric, only need to consider i2 <= i1
                (j1, j2) = (k - i1, k - i2)
                if j1 >= n or j2 >= n or grid[i1][j1] == -1 or grid[i2][j2] == -1:
                    continue
                current_max = -sys.maxsize
                next_steps = [(0, 0), (0, 1), (1, 0), (1, 1)]
                for next_step in next_steps:
                    (next_i1, next_j1, next_i2, next_j2) = (
                        i1 + next_step[0],
                        k + 1 - i1 - next_step[0],
                        i2 + next_step[1],
                        k + 1 - i2 - next_step[1],
                    )
                    if (
                        next_i1 < n  # out of bounds
                        and next_i2 < n
                        and next_j1 < n
                        and next_j2 < n
                        and grid[next_i1][next_j1] >= 0  # thorn
                        and grid[next_i2][next_j2] >= 0
                        and dp[next_i1][next_i2][k + 1] >= 0  # No route to (n-1, n-1)
                    ):
                        if dp[next_i1][next_i2][k + 1] > current_max:
                            current_max = dp[next_i1][next_i2][k + 1]
                if current_max >= 0:
                    dp[i1][i2][k] = current_max + (
                        grid[i1][j1]
                        if i1 == i2 and j1 == j2
                        else grid[i1][j1] + grid[i2][j2]
                    )

    return max(0, dp[0][0][0])


# Cherry Pickup ii
#
# grid[0:rows][0:cols] contain numbers of cherries in each cell.
# Two robots starting from (0,0) and (0, col-1). Robots can only
# move from (i,j) to (i+1, j') where j' is j-1, j, or j+1.
# Harvesting ends when both robots end at line rows - 1
# Return max number of cherries the two robots can harvest
#
# Constraints:
#   - 2 <= rows, cols <= 70
#   - 0 <= grid[i][j] <= 100
#
# Observation:
#   - We can synchronize the two robots without affecting final result.
#   - The two robots will always be on the same row when sync'ed
#     therefore, we can use [i, j1, j2] indicate a unique state in DP
#
# State Transition
#
# dp[i][j1][j2] = grid[i][j1]+grid[i][j2] + max(dp[i+1][j1-1,j1,j1+1][j2-1,j2,j2+1])
# Since row k only relies on row k+1, therefore we only
# need to memorized one row in this dp_current[j1][j2] and dp_next[j1][j2]
#
# leetcode_1463
def cherry_pickup_ii_dp(grid: List[List[int]]) -> int:
    (rows, cols) = (len(grid), len(grid[0]))
    dp_next = [[0 for j2 in range(cols)] for j1 in range(cols)]
    dp_current = [[0 for j2 in range(cols)] for j1 in range(cols)]
    for j1 in range(cols):
        for j2 in range(cols):
            dp_next[j1][j2] = (
                grid[rows - 1][j1]
                if j1 == j2
                else grid[rows - 1][j1] + grid[rows - 1][j2]
            )
    for i in range(rows - 2, -1, -1):
        for j1 in range(cols):
            for j2 in range(cols):
                valid_moves = [-1, 0, 1]
                current_max = -sys.maxsize
                if i == 1 and j1 == 1 and j2 == 2:
                    print(f"Stop here")
                for j1_move in valid_moves:
                    for j2_move in valid_moves:
                        j1_next = j1 + j1_move
                        j2_next = j2 + j2_move
                        if (
                            j1_next < 0
                            or j1_next >= cols
                            or j2_next < 0
                            or j2_next >= cols
                        ):
                            continue
                        if dp_next[j1_next][j2_next] > current_max:
                            current_max = dp_next[j1_next][j2_next]
                if current_max >= 0:
                    dp_current[j1][j2] = current_max + (
                        grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
                    )
        tmp = dp_next
        # Now dp_next points to the most recent result for i
        dp_next = dp_current
        dp_current = tmp
    return dp_next[0][cols - 1]


def test_cherry_pickup_i_dp():
    assert cherry_pickup_i_dp([[0, 1, -1], [1, 0, -1], [1, 1, 1]]) == 5
    assert cherry_pickup_i_dp([[1, 1, -1], [1, -1, 1], [-1, 1, 1]]) == 0


def test_cherry_pickup_ii_dp():
    assert (
        cherry_pickup_ii_dp([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]])
        == 22
    )
    assert cherry_pickup_ii_dp([[1, 1], [1, 1]]) == 4
