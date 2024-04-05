def test_0407():
    from .lc_0407 import Solution

    solution = Solution()
    assert (
        solution.trapRainWater(
            [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
        )
        == 4
    )

    assert (
        solution.trapRainWater(
            [
                [3, 3, 3, 3, 3],
                [3, 2, 2, 2, 3],
                [3, 2, 1, 2, 3],
                [3, 2, 2, 2, 3],
                [3, 3, 3, 3, 3],
            ]
        )
        == 10
    )

    assert (
        solution.trapRainWater(
            [
                [12, 13, 1, 12],
                [13, 4, 13, 12],
                [13, 8, 10, 12],
                [12, 13, 12, 12],
                [13, 13, 13, 13],
            ]
        )
        == 14
    )


def test_0462():
    from .lc_0462 import Solution

    solution = Solution()
    assert solution.minMoves2([1, 2, 3]) == 2
    assert solution.minMoves2([1, 0, 0, 8, 6]) == 14


def test_0475():
    from .lc_0475 import Solution

    solution = Solution()
    assert solution.find_radius([1, 2, 3], [2]) == 1
    assert solution.find_radius(houses=[1, 2, 3, 4], heaters=[1, 4]) == 1
    assert solution.find_radius(houses=[1, 5], heaters=[2]) == 3
