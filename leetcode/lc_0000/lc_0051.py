"""
51. N-Queens
Hard
Topics
Companies

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

 

Constraints:

    1 <= n <= 9
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        lineups: list[list[int]] = []

        # lineup: positioned queens at (i, lineup[i])
        def backtrack(lineup: list[int]) -> None:
            curr_row = len(lineup)
            if curr_row == n:
                lineups.append([i for i in lineup])
                return
            valid_cols = [i for i in range(n)]
            for i, j in enumerate(lineup):
                invalid_cols = [j, j + curr_row - i, j - (curr_row - i)]
                for invalid_col in invalid_cols:
                    if invalid_col in valid_cols:
                        valid_cols.remove(invalid_col)
            for valid_col in valid_cols:
                # backtrack([c for c in lineup] + [valid_col])
                lineup.append(valid_col)
                backtrack(lineup)
                lineup.pop()

        backtrack([])
        lineup_strs = [
            ["." * i + "Q" + "." * (n - i - 1) for i in lineup] for lineup in lineups
        ]
        return lineup_strs
