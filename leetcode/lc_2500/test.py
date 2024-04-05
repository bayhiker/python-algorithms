from pytest import mark


def test_2518():
    from .lc_2518 import Solution

    solution = Solution()
    assert solution.countPartitions([1, 2, 3, 4], 4)


def test_2546():
    from .lc_2546 import Solution

    solution = Solution()
    assert solution.makeStringsEqual("1010", "1001") is True
    assert solution.makeStringsEqual("11", "00") is False
