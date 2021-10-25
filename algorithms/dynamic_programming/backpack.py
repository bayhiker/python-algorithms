from typing import List

# Backpack i
# Given n items with size A[i], and an integer m denotes the size of a backpack.
# How full you can fill this backpack? You can't divide any items.
#
# lintcode_92
def backpack_i_recursive(m: int, A: List[int]) -> int:
    max_weight = 0
    for item in A:
        A_copy = A.copy()
        A_copy.remove(item)
        # If item is not included
        current_weight = backpack_i_recursive(m, A_copy)
        if current_weight > max_weight:
            max_weight = current_weight
        if item <= m:
            current_weight = item + backpack_i_recursive(m - item, A_copy)
            if current_weight > max_weight:
                max_weight = current_weight
    return max_weight


"""
# An alternative recursive implementation
def backpack_i_recursive(m: int, A: List[int]) -> int:
    def get_max_content(current_bag_weight, remaining_items: List[int]) -> int:
        if len(remaining_items) == 0:
            return current_bag_weight
        current_max = 0
        for item in remaining_items:
            remaining_items_copy = remaining_items.copy()
            remaining_items_copy.remove(item)
            # item not included in bag
            new_bag_weight = get_max_content(current_bag_weight, remaining_items_copy)
            if new_bag_weight > current_max:
                current_max = new_bag_weight
            # item included in bag
            if current_bag_weight + item <= m:
                new_bag_weight = get_max_content(
                    current_bag_weight + item, remaining_items_copy
                )
                if new_bag_weight > current_max:
                    current_max = new_bag_weight
        return current_max

    return get_max_content(0, A)
"""


#
# State Transition:
# dp[i][j] is max weight in bag when filling items A[0:i+1] to a bag with capacity j
# dp[i][j] = dp[i-1][j] if A[i] > j, else max(dp[i-1][j], A[i] + dp[i-1][j-A[i]])
# dp[0][j] = 0
#
# Time O(n**2), space O(n**2)
#
# lintcode_92
def backpack_i_dp(m: int, A: List[int]) -> int:
    n = len(A)
    dp = [[0 for j in range(m + 1)] for i in range(n)]
    for i in range(0, n):
        for j in range(1, m + 1):
            if A[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], A[i] + dp[i - 1][j - A[i]])
    return dp[n - 1][m]


# Backpack ii
# Fit items of size A[i] into a backpack of size m, V[i] is the value of item i.
# What's the max value that can fit into the backpack
#
# Constraints:
# - A[i], V[i], m are all integers
# - len(A) == len(V) == n
# - You can't split an item, each item can only be used once
# - 1 < m < 1000
# - n <= 100
#
# State transition:
# dp[i][j] is max value with items A[0:i+1] fitting into a bag of capacity j
# dp[i][j] = dp[i-1][j] if A[i]>j, else max(dp[i-1][j], V[i]+dp[i-1][j-A[i]])
#
# lintcode_125
def backpack_ii_dp(m: int, A: List[int], V: List[int]) -> int:
    n = len(A)
    dp = [[0 for j in range(m + 1)] for i in range(n)]
    for i in range(0, n):
        for j in range(1, m + 1):
            if A[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], V[i] + dp[i - 1][j - A[i]])
    return dp[n - 1][m]


def test_backpack_i_recursive():
    assert backpack_i_recursive(10, [3, 4, 8, 5]) == 9


def test_backpack_i_dp():
    assert backpack_i_dp(10, [3, 4, 8, 5]) == 9


def test_backpack_ii_dp():
    assert backpack_ii_dp(10, [2, 3, 5, 7], [1, 5, 2, 4]) == 9
    assert backpack_ii_dp(10, [2, 3, 8], [2, 5, 8]) == 10
