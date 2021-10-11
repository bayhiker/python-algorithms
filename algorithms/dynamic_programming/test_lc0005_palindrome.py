from algorithms.lib.test import duration
from .lc0005_palindrome import is_palindrome, get_longest_brute_force, get_longest_dp
import pytest
from time import time


def test_is_palindrom():
    assert not is_palindrome(None)
    assert not is_palindrome("")
    assert is_palindrome("a")
    assert not is_palindrome("ab")
    assert is_palindrome("aba")
    assert is_palindrome("abba")


def test_get_longest_brute_force():
    assert get_longest_brute_force("babad") == "bab"
    assert get_longest_brute_force("cbbd") == "bb"
    assert get_longest_brute_force("a") == "a"
    assert get_longest_brute_force("ac") == "a"


def test_get_longest_dp():
    assert get_longest_dp("babad") == "bab"
    assert get_longest_dp("cbbd") == "bb"
    assert get_longest_dp("a") == "a"
    assert get_longest_dp("ac") == "a"


def test_performance():
    s = "x" * 400
    duration_brute_force = duration(lambda: get_longest_brute_force(s))
    duration_dp = duration(lambda: get_longest_dp(s))
    print(f"dp is {duration_brute_force/duration_dp} faster then brute_force")
