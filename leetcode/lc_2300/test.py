from pytest import mark


def test_2334():
    from .lc_2334 import Solution

    solution = Solution()
    assert solution.validSubarraySize([1, 3, 4, 3, 1], 6) == 3


def test_2370():
    from .lc_2370 import Solution

    solution = Solution()
    assert solution.longestIdealString("acfgbd", 2) == 4
    assert solution.longestIdealString("abcd", 3) == 4
    assert solution.longestIdealString("lkpkxcigcs", 6) == 7


def test_2386():
    from .lc_2386 import Solution

    solution = Solution()
    assert solution.kSum([2, 4, -2], 5) == 2
    assert solution.kSum([1, -2, 3, 4, -10, 12], 16) == 10


def test_2344():
    from .lc_2344 import Solution

    solution = Solution()
    assert (
        solution.minOperations(nums=[2, 3, 2, 4, 3], numsDivide=[9, 6, 9, 3, 15]) == 2
    )

    assert solution.minOperations(nums=[4, 3, 6], numsDivide=[8, 2, 6, 10]) == -1
