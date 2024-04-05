def test_0509():
    from .lc_0509 import Solution

    solution = Solution()
    assert solution.fib(2) == 1
    assert solution.fib(3) == 2
    assert solution.fib(4) == 3


def test_0567():
    from .lc_0567 import Solution

    solution = Solution()
    assert solution.checkInclusion(s1="ab", s2="eidbaooo") is True
    assert solution.checkInclusion(s1="ab", s2="eidboaoo") is False
