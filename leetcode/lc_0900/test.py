def test_0907():
    from .lc_0907 import Solution

    solution = Solution()
    assert solution.sumSubarrayMins([3, 1, 2, 4]) == 17
    assert solution.sumSubarrayMins([11, 81, 94, 43, 3]) == 444


def test_0909():
    from .lc_0909 import Solution

    solution = Solution()
    assert (
        solution.snakesAndLadders(
            board=[
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ]
        )
        == 4
    )

    assert solution.snakesAndLadders(board=[[-1, -1], [-1, 3]]) == 1


def test_0945():
    from .lc_0945 import Solution

    solution = Solution()
    assert solution.minIncrementForUnique(nums=[1, 2, 2]) == 1
    assert solution.minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]) == 6


def test_0952():
    from .lc_0952 import Solution

    solution = Solution()
    """
    assert solution.largestComponentSize([4, 6, 15, 35]) == 4
    assert solution.largestComponentSize([20, 50, 9, 63]) == 2
    assert solution.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 29]) == 8
    assert solution.largestComponentSize([99, 68, 70, 77, 35, 52, 53, 25, 62]) == 8
    assert solution.largestComponentSize([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 6
    assert (
        solution.largestComponentSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        == 11
    )
    assert solution.largestComponentSize([98, 39, 14, 86, 56, 89, 26, 59, 63]) == 7
    """
    assert (
        solution.largestComponentSize([65, 35, 43, 76, 15, 11, 81, 22, 55, 92, 31]) == 9
    )


def test_0995():
    from .lc_0995 import Solution

    solution = Solution()
    # assert solution.minKBitFlips(nums=[0, 1, 0], k=1) == 2
    # assert solution.minKBitFlips(nums=[1, 1, 0], k=2) == -1
    # assert solution.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3) == 3
    assert solution.minKBitFlips(nums=[0, 1], k=2) == -1
