import pytest


def test_0001():
    from .lc_0001 import Solution

    solution: Solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]


def test_0051():
    from .lc_0051 import Solution

    solution: Solution = Solution()
    assert solution.solveNQueens(4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    assert solution.solveNQueens(1) == [["Q"]]


def test_0055():
    from .lc_0055 import Solution

    solution: Solution = Solution()
    assert solution.canJump([2, 3, 1, 1, 4]) is True
    assert solution.canJump([3, 2, 1, 0, 4]) is False


def test_0004():
    from .lc_0004 import Solution

    solution = Solution()
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2
    """
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert (
        solution.findMedianSortedArrays([1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11, 12])
        == 6.5
    )
    assert (
        solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12])
        == 6.5
    )
    assert (
        solution.findMedianSortedArrays([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12])
        == 6.5
    )
    assert solution.findMedianSortedArrays([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10]) == 6
    """
    solution.findMedianSortedArrays([], [1, 2, 3, 4, 5]) == 3


def test_0081():
    from .lc_0081 import Solution

    solution = Solution()
    assert solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0) is True
    assert solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3) is False
    assert solution.search(nums=[1, 0, 1, 1, 1], target=0) is True
    assert (
        solution.search(
            nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            target=13,
        )
        is True
    )
