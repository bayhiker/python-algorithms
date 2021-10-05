'''
You are given an array prices where prices[i] is the
price of a given stock on the ith day.

You want to maximize your profit by choosing a single
day to buy one stock and choosing a different day in
the future to sell that stock.

Return the maximum profit you can achieve from this
transaction. If you cannot achieve any profit, return 0.
'''

def get_profit_recursive(prices: 'list[float]'):
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
        if current_profit>max_profit:
            max_profit = current_profit
    return [max_profit, min_price]

'''
Qualifications for DP
The key here is to abstract max_profit problem to this: as we move from day 0 to day n-1,
find lowest stock price in prices[0:k]
- Overlapping subproblems: find_lowest(prices, k) and find_lowest(prices, k-1)
- Optimal substructure: max_profit(prices, k) can be calculated from max_profit(prices, k-1)
'''
def get_profit_dp_bottom_up(prices: 'list[float]'):
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

