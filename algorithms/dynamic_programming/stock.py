# leetcode_121_122_123_188
from typing import List

"""
You are given an array prices where prices[i] is the
price of a given stock on the ith day.

You want to maximize your profit by choosing a single
day to buy one stock and choosing a different day in
the future to sell that stock.

Return the maximum profit you can achieve from this
transaction. If you cannot achieve any profit, return 0.
"""

# leetcode_121
def get_profit_recursive(prices: List[float]):
    # returns [max_profit, min_price]
    if not prices or len(prices) == 0:
        return [0, -1]
    if len(prices) == 1:
        return [0, prices[0]]
    last_day = len(prices) - 1
    last_day_price = prices[last_day]
    [max_profit, min_price] = get_profit_recursive(prices[0:last_day])
    if last_day_price <= min_price:
        min_price = last_day_price
        # max_profit stays at current value
    else:
        current_profit = last_day_price - min_price
        if current_profit > max_profit:
            max_profit = current_profit
    return [max_profit, min_price]


"""
Qualifications for DP
The key here is to abstract max_profit problem to this: as we move from day 0 to day n-1,
find lowest stock price in prices[0:k]
- Overlapping subproblems: find_lowest(prices, k) and find_lowest(prices, k-1)
- Optimal substructure: max_profit(prices, k) can be calculated from max_profit(prices, k-1)
"""
# leetcode_121
def get_profit_dp_bottom_up(prices: "list[float]"):
    # Use two pointers buy_date and sell_date:
    # buy_date points to the previous lowest price before today
    # sell_date points to sell date to maximize profit from stock purchased on buy_date.
    # As we move buy_date forward, buy_date is reset every time we see a even lower price
    if not prices or len(prices) == 0:
        return 0
    buy_date = 0
    max_profit = 0
    for today in range(1, len(prices)):
        if prices[today] <= prices[buy_date]:
            buy_date = today
        else:
            current_profit = prices[today] - prices[buy_date]
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit


# prices[i] is price of a stock on i'th day
# Find the most profit you can make with at most k transactions.
# Each transaction here is a combo of buy one day and then sell on a later date.
# You cannot hold stocks from more than one transactions, sell before you purchase.
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
def get_max_profit_dp(prices: List[float], k: int):
    total_days = len(prices)
    if total_days < 2:
        return 0
    # If k is more than half of total days, then use greedy algorithm
    if k > len(prices) // 2:
        return get_max_profit_greedy(prices)

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


# No limit on number of transactions, only restraint it that you have to
# sell stock on hand before making your next buy
# leetcode_122
def get_max_profit_greedy(prices: List[float]):
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


# leetcode_188
def get_max_profit_recursive(prices: List[float], k: int):
    if len(prices) <= 1 or k == 0:
        return 0
    prices_copy = prices.copy()
    # If there's no transaction happening on last day
    max_profit = get_max_profit_recursive(prices_copy[0 : len(prices_copy) - 1], k)
    # Otherwise if sell of last transaction happens on last day
    for i in range(0, len(prices_copy)):
        # If buy action of last transaction happens on day i
        last_tx_profit = prices_copy[len(prices_copy) - 1] - prices_copy[i]
        prev_max_profit = get_max_profit_recursive(prices_copy[0:i], k - 1)
        if last_tx_profit + prev_max_profit > max_profit:
            max_profit = last_tx_profit + prev_max_profit
    return max_profit


from ..lib.test import duration


def test_stock_recursive():
    assert get_profit_recursive([7, 1, 5, 3, 6, 4])[0] == 5
    assert get_profit_recursive([7, 6, 4, 3, 1])[0] == 0
    assert get_profit_dp_bottom_up([7, 1, 5, 3, 6, 4]) == 5
    assert get_profit_dp_bottom_up([7, 6, 4, 3, 1]) == 0


def test_max_profit_greedy():
    assert get_max_profit_greedy([2, 4, 1]) == 2
    assert get_max_profit_greedy([3, 2, 6, 5, 0, 3]) == 7
    assert get_max_profit_greedy([7, 1, 5, 3, 6, 4]) == 7
    assert get_max_profit_greedy([1, 2, 3, 4, 5]) == 4
    assert get_max_profit_greedy([7, 6, 4, 3, 1]) == 0
    assert get_max_profit_greedy([1, 2, 1, 3]) == 3
    assert get_max_profit_greedy([1, 2, 1, 3, 2]) == 3


def test_max_profit_dp():
    assert get_max_profit_dp([2, 4, 1], 2) == 2
    assert get_max_profit_dp([3, 2, 6, 5, 0, 3], 2) == 7
    assert get_max_profit_dp([3, 2, 6, 5, 0, 3], 1) == 4


def test_max_profit_recursive():
    assert get_max_profit_recursive([2, 4, 1], 2) == 2
    assert get_max_profit_recursive([3, 2, 6, 5, 0, 3], 2) == 7
    assert get_max_profit_recursive([3, 2, 6, 5, 0, 3], 1) == 4


def test_performance():
    prices = [3, 2, 6, 5, 0, 3] * 2
    duration_dp = duration(lambda: get_max_profit_dp(prices, 100))
    duration_recursive = duration(lambda: get_max_profit_recursive(prices, 100))
    print(f"DP duration {duration_dp}, recursive duration {duration_recursive}")
    print(f"DP was {duration_recursive/duration_dp} times faster")
