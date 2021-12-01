# leetcode_121_122_123_188
from typing import List

# Best time to buy and sell stock
# Given prices[i] as the price of a given stock, return the max profit
# to buy the stock and sell on a different day
# leetcode_121
def stocks_i_recursive(prices: List[float]):
    # returns [max_profit, min_price]
    if not prices or len(prices) == 0:
        return [0, -1]
    if len(prices) == 1:
        return [0, prices[0]]
    last_day = len(prices) - 1
    last_day_price = prices[last_day]
    [max_profit, min_price] = stocks_i_recursive(prices[0:last_day])
    if last_day_price <= min_price:
        min_price = last_day_price
        # max_profit stays at current value
    else:
        current_profit = last_day_price - min_price
        if current_profit > max_profit:
            max_profit = current_profit
    return [max_profit, min_price]


# Use DP to solve leetcode_121
# State transition:
# dp[i]: max profit on i'th day
# dp[0] = 0
# p pointer to lowest price during prices[0:i]
# dp[i+1] = max(dp[i], prices[i+1] - prices[p]): dp[i] if buy or stay put on day i+1, or
#             prices[i+1] - prices[p] if sell.
# Because dp[i+1] only depends on state dp[i], therefore dp array can be replaced with a variable
#
# leetcode_121
def stocks_i_dp_bottom_up(prices: "list[float]"):
    if not prices or len(prices) == 0:
        return 0
    lowest = 0
    max_profit = 0
    for today in range(1, len(prices)):
        if prices[today] <= prices[lowest]:
            lowest = today
        else:
            max_profit = max(max_profit, prices[today] - prices[lowest])
    return max_profit


# No limit on number of transactions, only restraint it that you have to
# sell stock on hand before making your next buy
# leetcode_122
def stocks_ii_greedy(prices: List[float]):
    max_profit = 0
    buy_date = 0
    today = 0
    total_days = len(prices)
    while today < total_days:
        if today == total_days - 1:
            max_profit += (
                prices[today] - prices[buy_date]
                if prices[today] > prices[buy_date]
                else 0
            )
            break
        while today < total_days - 1 and prices[today] >= prices[today + 1]:
            buy_date = today + 1
            today += 1
        while today < total_days - 1 and prices[today] <= prices[today + 1]:
            sell_date = today + 1
            today += 1
        if today == total_days - 1:
            continue
        expected_profit = prices[sell_date] - prices[buy_date]
        max_profit += expected_profit if expected_profit > 0 else 0
        today += 1
        buy_date = today
    return max_profit


# Use DP to solve leetcode_122
# dp[i]: max profit so far
# dp[0]: 0
# p pointer prices[p-1] >= prices[p] and prices[p] < prices[p+1] < ... < prices[i]
# dp[i+1] = dp[i] if p == i (cannot sell)
#           dp[i] + prices[i+1] - prices[p] if p < i
# leetcode_122
def stocks_ii_dp(prices: List[int]) -> int:
    p = 0
    n = len(prices)
    max_p = 0
    max_total = 0
    for i in range(1, n):
        if prices[i] <= prices[i - 1]:
            p = i
            max_p = max_total
        else:
            max_total = max_p + prices[i] - prices[p]
    return max_total


# Best Time to Buy and Sell Stock III
# prices[i] is the stock price on i'th day, find max profit if you can complete
# at most two transactions
#
# State transition is an extension to stocks_i with one transaction:
# dp[i]: max profit days 0 to i with one transaction
# p pointer to lowest price so far seen
# dp[i] = max(dp[i-1], prices[i] - prices[p]): either there's a sell on day i, or not
# Then go through dp[1:n], if dp[i] < dp[i-1], then there's a sell on day i
# find max profit for prices[i+1:n], then you get total profit if first sell is on day i
# Repeat for all such i, find the largest profit
#
# Time: O(n**2), space: O(n)
#
# leetcode_123
def stocks_iii_dp(prices: List[int]) -> int:
    n = len(prices)
    buy_date = 0
    dp = [0 for i in range(n)]
    for i in range(1, n):
        if prices[i] < prices[buy_date]:
            buy_date = i

    pass


# leetcode_188
def stocks_iv_recursive(prices: List[float], k: int):
    if len(prices) <= 1 or k == 0:
        return 0
    prices_copy = prices.copy()
    # If there's no transaction happening on last day
    max_profit = stocks_iv_recursive(prices_copy[0 : len(prices_copy) - 1], k)
    # Otherwise if sell of last transaction happens on last day
    for i in range(0, len(prices_copy)):
        # If buy action of last transaction happens on day i
        last_tx_profit = prices_copy[len(prices_copy) - 1] - prices_copy[i]
        prev_max_profit = stocks_iv_recursive(prices_copy[0:i], k - 1)
        if last_tx_profit + prev_max_profit > max_profit:
            max_profit = last_tx_profit + prev_max_profit
    return max_profit


# Best Time to Buy and Sell Stocks iv
#
# prices[i] is price of a stock on i'th day
# Find the most profit you can make with at most k transactions.
# Each transaction here is a combo of buy one day and then sell on a later date.
# You cannot hold stocks from more than one transactions, sell before you purchase.
#
# State Transition:
#
# DP state transition 1:
# https://soulmachine.gitbooks.io/algorithm-essentials/content/java/dp/best-time-to-buy-and-sell-stock-iv.html
# local optimal profit local[i][j], must perform j'th trans of sell on day i
# local[i][j] = max(global[i-1][j-1] + max(diff,0), local[i-1][j]+diff)
# global optimal profit global[i][j], max profit on day i with j transactions.
# j'th transaction doesn't have to happen on day i
# global[i][j] = max(local[i][j], global[i-1][j])
#
# DP state transition 2:
# https://www.hrwhisper.me/leetcode-best-time-to-buy-and-sell-stock-i-ii-iii-iv/
# dp[i][x] = max(dp[i-1][x] , dp[j][x - 1] + prices[i] - prices[j])  0 <= j < i
# Max profit for i'th day x trans is the larger of
# (1) No sell transaction on day i, dp[i-1][x]
# (2) Sell on day i, then loop through buy day of 0 to i, find max profit
#
# State transition 2 seems more straightforward
# leetcode 188
def stocks_iv_dp(prices: List[float], k: int):
    total_days = len(prices)
    if total_days < 2:
        return 0
    # If k is more than half of total days, then use greedy algorithm
    if k > len(prices) // 2:
        return stocks_ii_greedy(prices)

    # dp[i][j]: max profit on i'th day with j or less transactions.
    # There may or may not be any tx on i'th day
    # Transaction index k goes from 0 to k (not k-1)
    dp = [[0 for x in range(0, k + 1)] for i in range(0, len(prices))]
    for i in range(0, len(prices)):
        if i == 0:
            # dp[0][x] stays 0 as initialized
            continue
        for x in range(0, k + 1):
            if x == 0:
                # dp[i][0] should be 0 as initialized
                continue
            dp[i][x] = dp[i - 1][x]  # If no transaction on day i
            for j in range(0, i):
                # Assuming x'th tx is buy on j'th day and sell on i'th day
                x_tx_profit = prices[i] - prices[j]
                if dp[j][x - 1] + x_tx_profit > dp[i][x]:
                    dp[i][x] = dp[j][x - 1] + x_tx_profit
    return dp[total_days - 1][k]


from ..lib.test import duration


def test_stocks_i():
    assert stocks_i_recursive([7, 1, 5, 3, 6, 4])[0] == 5
    assert stocks_i_recursive([7, 6, 4, 3, 1])[0] == 0
    assert stocks_i_dp_bottom_up([7, 1, 5, 3, 6, 4]) == 5
    assert stocks_i_dp_bottom_up([7, 6, 4, 3, 1]) == 0


def test_stocks_ii_greedy():
    assert stocks_ii_greedy([2, 4, 1]) == 2
    assert stocks_ii_greedy([3, 2, 6, 5, 0, 3]) == 7
    assert stocks_ii_greedy([7, 1, 5, 3, 6, 4]) == 7
    assert stocks_ii_greedy([1, 2, 3, 4, 5]) == 4
    assert stocks_ii_greedy([7, 6, 4, 3, 1]) == 0
    assert stocks_ii_greedy([1, 2, 1, 3]) == 3
    assert stocks_ii_greedy([1, 2, 1, 3, 2]) == 3


def test_stocks_ii_dp():
    assert stocks_ii_dp([2, 4, 1]) == 2
    assert stocks_ii_dp([3, 2, 6, 5, 0, 3]) == 7
    assert stocks_ii_dp([7, 1, 5, 3, 6, 4]) == 7
    assert stocks_ii_dp([1, 2, 3, 4, 5]) == 4
    assert stocks_ii_dp([7, 6, 4, 3, 1]) == 0
    assert stocks_ii_dp([1, 2, 1, 3]) == 3
    assert stocks_ii_dp([1, 2, 1, 3, 2]) == 3


def test_stocks_iv_recursive():
    assert stocks_iv_recursive([2, 4, 1], 2) == 2
    assert stocks_iv_recursive([3, 2, 6, 5, 0, 3], 2) == 7
    assert stocks_iv_recursive([3, 2, 6, 5, 0, 3], 1) == 4


def test_stocks_iv_dp():
    assert stocks_iv_dp([2, 4, 1], 2) == 2
    assert stocks_iv_dp([3, 2, 6, 5, 0, 3], 2) == 7
    assert stocks_iv_dp([3, 2, 6, 5, 0, 3], 1) == 4


def test_performance():
    prices = [3, 2, 6, 5, 0, 3] * 2
    duration_dp = duration(lambda: stocks_iv_dp(prices, 100))
    duration_recursive = duration(lambda: stocks_iv_recursive(prices, 100))
    print(f"DP duration {duration_dp}, recursive duration {duration_recursive}")
    print(f"DP was {duration_recursive/duration_dp} times faster")
