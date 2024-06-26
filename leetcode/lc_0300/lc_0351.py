"""
Android Unlock Patterns

Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

 

Rules for a valid pattern:

    Each pattern must connect at least m keys and at most n keys.
    All the keys must be distinct.
    If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
    The order of keys used matters.

 

 

Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

 

Example:

Input: m = 1, n = 1
Output: 9

"""


class Solution(object):
    def numberOfPatterns(self, m, n):
        return self.number_of_patterns(m, n)

    def number_of_patterns(self, m, n):
        # Observation 1: 1,3,7,9 and 2,4,6,8 are symmetric, therefore,
        # we only need to find valid patterns from 1, 2, and 5.
        # Observation 2: For each starting number 1,2,5, use the following DFS to traverse and count
        #      dfs(m,n,prev:int,visited:list[int], length)
        # Observation 3: Invalid next numbers:
        #    i + prev == 10 and 5 not visited: e.g. 19/37/28/46
        #    prev/i corners on same row and (prev+i)/2 not in visited: e.g. 13/79/17/39
        pass
