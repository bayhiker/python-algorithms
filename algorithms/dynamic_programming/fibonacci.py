def fib_recursion(n):
    if n < 0:
        raise ValueError(f"n must be non-negative, found {n}")
    return n if n < 2 else fib_recursion(n - 1) + fib_recursion(n - 2)


def fib_dp_bottom_up(n):
    if n < 0:
        raise ValueError(f"n must be non-negative, found {n}")
    if n < 2:
        return n
    fib = 1
    prev = 0
    for counter in range(2, n):
        fib = fib + prev
        prev = fib - prev
    return fib + prev


def fib_dp_top_down(n):
    if n < 0:
        raise ValueError(f"n must be non-negative, found {n}")
    fib = {0: 0, 1: 1}

    def get_fib(k):
        if k in fib:
            return fib[k]
        fib[k] = get_fib(k - 1) + get_fib(k - 2)
        return fib[k]

    return get_fib(n)


class FibDpTopDown:
    def __init__(self) -> None:
        self.fib = {0: 0, 1: 1}

    def get_fib(self, n):
        if n < 0:
            raise ValueError(f"n must be non-negative, found {n}")
        if n in self.fib:
            return self.fib[n]
        else:
            self.fib[n] = self.get_fib(n - 1) + self.get_fib(n - 2)
            return self.fib[n]


import pytest
from lib.test import duration


def test_fib_recursion():
    with pytest.raises(ValueError):
        fib_recursion(-1)
    assert (fib_recursion(0), 0)
    assert (fib_recursion(1), 1)
    assert (fib_recursion(2), 1)
    assert (fib_recursion(10), 55)


def test_fib_dp_bottom_up():
    with pytest.raises(ValueError):
        fib_dp_bottom_up(-1)
    assert (fib_dp_bottom_up(0), 0)
    assert (fib_dp_bottom_up(1), 1)
    assert (fib_dp_bottom_up(2), 1)
    assert (fib_dp_bottom_up(10), 55)


def test_fib_dp_top_down_method():
    with pytest.raises(ValueError):
        fib_dp_top_down(-1)
    assert (fib_dp_top_down(0), 0)
    assert (fib_dp_top_down(1), 1)
    assert (fib_dp_top_down(2), 1)
    assert (fib_dp_top_down(10), 55)


def test_fib_dp_top_down_class():
    fibDpTopDown = FibDpTopDown()
    with pytest.raises(ValueError):
        fibDpTopDown.get_fib(-1)
    assert (fibDpTopDown.get_fib(0), 0)
    assert (fibDpTopDown.get_fib(1), 1)
    assert (fibDpTopDown.get_fib(2), 1)
    assert (fibDpTopDown.get_fib(10), 55)


def test_performance():
    n = 10 ^ 40
    duration_recursion = duration(lambda: fib_recursion(n))
    print(f"Fib execution time with recursion was {duration_recursion}")
    duration_dp_bottom_up = fib_dp_bottom_up(n)
    print(f"Fib execution time with dp_bottom_up was {duration_dp_bottom_up}")
    print(
        f"dp_bottom_up was faster by {duration_recursion/duration_dp_bottom_up} times"
    )

    duration_dp_top_down_method = duration(lambda: fib_dp_top_down(n))
    print(
        f"Fib execution time with fib_db_top_down method was {duration_dp_top_down_method}"
    )
    print(
        f"dp_top_down method was faster by {duration_recursion/duration_dp_top_down_method} times"
    )

    fibDpTopDown = FibDpTopDown()
    duration_dp_top_down_class = duration(lambda: fib_dp_top_down(n))
    print(f"Fib execution time with FibDpTopDown was {duration_dp_top_down_class}")
    print(
        f"dp_top_down class was faster by {duration_recursion/duration_dp_top_down_class} times"
    )
