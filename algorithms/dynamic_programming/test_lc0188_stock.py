from .lc0188_stock import (
    get_max_profit_dp,
    get_max_profit_greedy,
    get_max_profit_recursive,
)

from ..lib.test import duration


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
