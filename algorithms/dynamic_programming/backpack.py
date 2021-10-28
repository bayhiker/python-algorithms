from typing import List
import sys

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


# Backpack iii
# Given a backpack of capacity m, and n items with weight A[i] and value V[i]
# Each item can be used an infinite number of numbers. Return the max value
# in the backpack
#
# State Transition
# dp[i][j] is max value with items A[0:i+1] fitting into bag of capacity j
# dp[i][j] = max(x*V[i] + dp[i-1][j-x*A[i]]) for all 0 <= x*A[i] <= j
#
# lintcode_440
def backpack_iii_dp(m: int, A: List[int], V: List[int]) -> int:
    n = len(A)
    if n == 0:
        return 0
    dp = [[0 for j in range(m + 1)] for i in range(n)]
    for i in range(n):
        for j in range(1, m + 1):
            for k in range(j // A[i] + 1):
                v = k * V[i] + dp[i - 1][j - k * A[i]]
                if v > dp[i][j]:
                    dp[i][j] = v
    return dp[n - 1][m]


# Backpack iv
# n items each weighing nums[i], return number of ways to fill a
# bag of capacity target. Item can be used more than once.
#
# dp[i][j]: number of ways to fill bag of size j with nums[0:i+1]
# dp[i][j] = sum(dp[i-1][j-nums[i]*k]) for all 0<=nums[i]*k<=j
# dp[0][j] = 0
#
# lintcode_562
def backpack_iv_dp(nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp = [[0 for j in range(target + 1)] for i in range(n)]
    for i in range(n):
        for j in range(1, target + 1):
            for k in range(j // nums[i] + 1):
                if k * nums[i] == j:
                    dp[i][j] += 1
                else:
                    dp[i][j] = dp[i][j] + dp[i - 1][j - k * nums[i]]
    return dp[n - 1][target]


# Backpack v
# n items with weight nums[i], backpack capacity target.
# Each item can only be used at most once, return number of ways to
# fill the backpack
#
# State Transition:
# dp[i][j]: ways to use nums[0:i+1] to fill backpack of target j
# dp[i][j] = dp[i-1][j] if nums[i]>j
#            else dp[i-1][j] + 1 if nums[i] == j
#            elif dp[i-1][j-nums[i]] + dp[i-1][j]
# Improvement: during state transition, only dp[i-1] is needed.
#     therefore, only need to remember one row of dp
#
# lintcode_563
def backpack_v_dp(nums: List[int], target: int) -> int:
    n = len(nums)
    dp_prev = [0 for j in range(target + 1)]
    dp_current = [0 for j in range(target + 1)]
    for i in range(n):
        for j in range(1, target + 1):
            if nums[i] > j:
                dp_current[j] = dp_prev[j]
            elif nums[i] == j:
                dp_current[j] = dp_prev[j] + 1
            else:
                dp_current[j] = dp_prev[j - nums[i]] + dp_prev[j]
        tmp = dp_prev
        dp_prev = dp_current
        dp_current = tmp
    return dp_prev[target]


# Backpack vi
# nums[i] all positive and no duplicates. Find the number of ways to
# exactly add nums[i] up to m. Numbers can be used multiple times,
# different orderings are counted as different solutions.
#
# State Transition:
# This is actually a combination sum problem.
# dp[i]: Number of ways to add up to i
# dp[0] == 0
# dp[i] = sum(dp[i-nums[j]]) for all i in range(n) nums[j] <= i
#
# Note that we are looping thru target number first, then each num.
# This takes care of the permutation issue: 1,2 and 2,1 are different.
# For example, if nums is [1,2], and m is 3:
# dp[0]: ()
# dp[1]: (1)
# dp[2]: (1,1) (from dp[2-1]), (2) (from dp[2-2])
# dp[3]: (1,1,1), (2,1) (dp[3-1]), (1,2) (from dp[3-2])
#
#
# lintcode_not_found
def backpack_vi_dp(nums: List[int], target: int) -> int:
    n = len(nums)
    dp = [0 for i in range(target + 1)]
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]
    return dp[target]


# Backpack vii
# You have n dollars, bags of rice are sold at prices[i] with weights[i]
# and available amounts[i], return the max weight of rice you can buy
#
# State Transition:
# dp[i][j]: max rice weight with prices[0:i+1] and j dollars
# dp[i][0] = 0
# dp[i][j] = dp[i-1][j] if prices[i] > j else max(dp[i-1][j-k*prices[i]] + k*weight[i])
#      for k*prices[i] >= 0 and k*prices[i] <= j and k <= amounts[i]
# This problem is similar to Backpack iii but with amount limit
# leetcode_798 (beat 98.60%)
def backpack_vii_dp(
    n: int, prices: List[int], weights: List[int], amounts: List[int]
) -> int:
    varieties = len(prices)
    if varieties == 0:
        return 0
    dp_current = [0 for i in range(n + 1)]
    dp_prev = [0 for i in range(n + 1)]
    for i in range(varieties):
        for j in range(1, n + 1):
            for k in range(j // prices[i] + 1):
                if k > amounts[i]:
                    break
                total = k * weights[i] + dp_prev[j - k * prices[i]]
                if total > dp_current[j]:
                    dp_current[j] = total
        dp_current, dp_prev = dp_prev, dp_current
    return dp_prev[n]


# Backpack viii
# Given n coins of amounts[i] and values[i], return number of different combination
# values no more than m
#
# State transition:
#
# dp[i]: i is a valid combination value
# dp[0] = True
# dp[i] = or(dp[i-j*values[j]]) for i in range(n), 0<j<=amounts[i], i-j*values[i] >= 0
#
# lintcode_799
def backpack_viii_dp(target: int, values: List[int], amounts: List[int]) -> int:
    n = len(values)
    dp_prev = [True if i == 0 else False for i in range(target + 1)]
    dp_current = [False for i in range(target + 1)]
    # No infinite reuse of items, iterate over n first, then target+1
    for i in range(n):
        for j in range(0, target + 1):
            if dp_prev[j]:
                dp_current[j] = True
                continue
            for k in range(1, amounts[i] + 1):
                if k * values[i] > j:
                    break
                if dp_prev[j - k * values[i]]:
                    dp_current[j] = True
                    break
        dp_prev, dp_current = dp_current, dp_prev
    return len(list(filter(lambda valid: valid, dp_prev[1 : target + 1])))


# Backpack ix
# Use m dollar to apply for a subset of n colleges with app fee prices[i]
# and admission probabilities[i]. Return the max probability of getting
# at least one admission.
#
# State Transition:
# dp[i][j]: max prob of applying for schools 0:i+1, with max of j dollars
# dp[i][j] = dp[i-1][j] if prices[i] > j else max(prob[i] + dp[i-1][j-prices[i]], dp[i-1][j])
#
# lintcode_800
def backpack_ix_dp(m: int, prices: List[int], probabilities: List[float]) -> float:
    n = len(prices)
    dp_prev = [0 for i in range(m + 1)]
    dp_current = [0 for i in range(m + 1)]
    for i in range(n):
        for j in range(1, m + 1):
            dp_current[j] = (
                dp_prev[j]
                if prices[i] > j
                else max(
                    1 - (1 - probabilities[i]) * (1 - dp_prev[j - prices[i]]),
                    dp_prev[j],
                )
            )
        dp_current, dp_prev = dp_prev, dp_current
    return dp_prev[m]


# Backpack x
# You have m dollars, and the merchant has three types of goods priced at 150,
# 250, and 300. Assuming there are unlimited number of each goods, and whatever
# money is left will be tipped to the merchant. Return the least amount of tip.
#
# State transition:
# dp[i][j]: tip with goods prices[0:i+1] and j dollars
# dp[i][0]: 0
# dp[i][j] = min(dp[i-1][j-k*prices[i]]) 0<=k*prices[i]<=j
#
# lintcode_801
def backpack_x_dp(m: int, prices: List[int] = [150, 250, 350]) -> int:
    dp_prev = [i for i in range(m + 1)]
    dp_current = [i for i in range(m + 1)]
    for i in range(len(prices)):
        for j in range(1, m + 1):
            for k in range(j // prices[i] + 1):
                current_tip = dp_prev[j - k * prices[i]]
                if dp_current[j] > current_tip:
                    dp_current[j] = current_tip
        dp_current, dp_prev = dp_prev, dp_current
        # Most recent valid result is now stored in dp_prev
    return dp_prev[m]


def test_backpack_i_recursive():
    assert backpack_i_recursive(10, [3, 4, 8, 5]) == 9


def test_backpack_i_dp():
    assert backpack_i_dp(10, [3, 4, 8, 5]) == 9


def test_backpack_ii_dp():
    assert backpack_ii_dp(10, [2, 3, 5, 7], [1, 5, 2, 4]) == 9
    assert backpack_ii_dp(10, [2, 3, 8], [2, 5, 8]) == 10


def test_backpack_iii_dp():
    assert backpack_iii_dp(100, [], []) == 0
    assert backpack_iii_dp(10, [2, 3, 5, 7], [1, 5, 2, 4]) == 15


def test_backpack_iv_dp():
    assert backpack_iv_dp([2, 3, 6, 7], 7) == 2
    assert backpack_iv_dp([2, 3, 4, 5], 7) == 3


def test_backpack_v_dp():
    assert backpack_v_dp([1, 2, 3, 3, 7], 7) == 2


def test_backpack_vi_dp():
    assert backpack_vi_dp([1, 2], 3) == 3
    assert backpack_vi_dp([1, 2, 4], 4) == 6


def test_backpack_vii_dp():
    assert backpack_vii_dp(8, [3, 2], [300, 160], [1, 6]) == 640
    assert backpack_vii_dp(8, [2, 4], [100, 100], [4, 2]) == 400


def test_backpack_viii_dp():
    assert backpack_viii_dp(5, [1, 4], [2, 1]) == 4
    assert backpack_viii_dp(10, [1, 2, 4], [2, 1, 1]) == 8


def test_backpack_ix_dp():
    # float numbers may not be exactly equal to reference answer
    assert backpack_ix_dp(10, [4, 4, 5], [0.1, 0.2, 0.3]) - 0.440 < 10 ** -3
    assert backpack_ix_dp(10, [4, 5, 6], [0.1, 0.2, 0.3]) - 0.370 < 10 ** -3


def test_backpack_x_dp():
    assert backpack_x_dp(900) == 0
    assert backpack_x_dp(800) == 0
    assert backpack_x_dp(3) == 3
