from .fibonacci import fib_recursion, fib_dp_bottom_up, FibDpTopDown, fib_dp_top_down
import pytest
import time

def test_fib_recursion():
    with pytest.raises(ValueError):
        fib_recursion(-1)
    assert(fib_recursion(0), 0)
    assert(fib_recursion(1), 1)
    assert(fib_recursion(2), 1)
    assert(fib_recursion(10), 55)

def test_fib_dp_bottom_up():
    with pytest.raises(ValueError):
        fib_dp_bottom_up(-1)
    assert(fib_dp_bottom_up(0), 0)
    assert(fib_dp_bottom_up(1), 1)
    assert(fib_dp_bottom_up(2), 1)
    assert(fib_dp_bottom_up(10), 55)

def test_fib_dp_top_down_method():
    with pytest.raises(ValueError):
        fib_dp_top_down(-1)
    assert(fib_dp_top_down(0), 0)
    assert(fib_dp_top_down(1), 1)
    assert(fib_dp_top_down(2), 1)
    assert(fib_dp_top_down(10), 55)

def test_fib_dp_top_down_class():
    fibDpTopDown = FibDpTopDown()
    with pytest.raises(ValueError):
        fibDpTopDown.get_fib(-1)
    assert(fibDpTopDown.get_fib(0), 0)
    assert(fibDpTopDown.get_fib(1), 1)
    assert(fibDpTopDown.get_fib(2), 1)
    assert(fibDpTopDown.get_fib(10), 55)

def test_performance():
    n = 10^40
    start_time = time.time()
    fib_from_recursion = fib_recursion(n)
    duration_recursion = time.time() - start_time
    print(f"Fib execution time with recursion was {duration_recursion}")

    start_time = time.time()
    fib_from_dp_bottom_up = fib_dp_bottom_up(n)
    duration_dp_bottom_up = time.time() - start_time
    print(f"Fib execution time with dp_bottom_up was {duration_dp_bottom_up}")
    print(f"dp_bottom_up was faster by {duration_recursion/duration_dp_bottom_up} times")
    assert(fib_from_dp_bottom_up == fib_from_recursion)

    start_time = time.time()
    fib_from_dp_top_down_method = fib_dp_top_down(n)
    duration_dp_top_down_method = time.time() - start_time
    print(f"Fib execution time with fib_db_top_down method was {duration_dp_top_down_method}")
    print(f"dp_top_down method was faster by {duration_recursion/duration_dp_top_down_method} times")
    assert(fib_from_dp_top_down_method == fib_from_recursion)

    fibDpTopDown = FibDpTopDown()
    start_time = time.time()
    fib_from_dp_top_down_class = fib_dp_top_down(n)
    duration_dp_top_down_class = time.time() - start_time
    print(f"Fib execution time with FibDpTopDown was {duration_dp_top_down_class}")
    print(f"dp_top_down class was faster by {duration_recursion/duration_dp_top_down_class} times")
    assert(fib_from_dp_top_down_class == fib_from_recursion)