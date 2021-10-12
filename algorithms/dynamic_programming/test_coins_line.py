from .coins_line import (
    first_wins_recursive,
    first_wins_dp,
    first_wins_math,
    first_wins_with_values_dp,
    first_wins_left_right_dp,
)
from ..lib.test import duration


def test_first_wins_recursive():
    assert first_wins_recursive(1)
    assert first_wins_recursive(4)
    assert not first_wins_recursive(9)
    assert first_wins_recursive(10)
    assert first_wins_recursive(11)
    assert not first_wins_recursive(12)


def test_first_wins_dp():
    assert first_wins_dp(1)
    assert first_wins_dp(4)
    assert not first_wins_dp(9)
    assert first_wins_dp(10)
    assert first_wins_dp(11)
    assert not first_wins_dp(12)


def test_performance():
    n = 40
    duration_recursive = duration(lambda: first_wins_recursive(n))
    duration_dp = duration(lambda: first_wins_dp(n))
    print(
        f"n is {n}, duration_dp is {duration_dp} and is {duration_recursive/duration_dp} faster than recursive"
    )

    n = 100
    duration_math = duration(lambda: first_wins_math(n))
    print(
        f"n is {n}, duration_math is {duration_dp} and is {duration_dp/duration_math} faster than dp"
    )


def test_first_wins_with_values_dp():
    assert first_wins_with_values_dp([1, 2, 2])
    assert not first_wins_with_values_dp([1, 2, 4])
    assert not first_wins_with_values_dp([1, 2, 4, 1, 2, 4])


def test_first_wins_left_right_dp():
    assert first_wins_left_right_dp([3, 2, 2])
    assert first_wins_left_right_dp([1, 2, 4])
    assert not first_wins_left_right_dp([1, 20, 4])
    assert first_wins_left_right_dp([3, 2, 2, 2])
    assert first_wins_left_right_dp([3, 2, 1, 2, 3])
    assert not first_wins_left_right_dp([3, 2, 1, 100, 3])
    assert first_wins_left_right_dp([3, 2, 1, 100, 3, 100])
    assert first_wins_left_right_dp([3, 2, 2, 1, 100, 100])
    assert not first_wins_left_right_dp([2, 2, 2, 2, 100, 100])
