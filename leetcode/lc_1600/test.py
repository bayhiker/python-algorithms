def test_1615():
    from .lc_1615 import Solution

    solution = Solution()
    assert solution.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]) == 4
    assert (
        solution.maximalNetworkRank(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]])
        == 5
    )

    assert (
        solution.maximalNetworkRank(
            n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
        )
        == 5
    )


def test_1620():
    from .lc_1620 import Solution

    solution = Solution()
    """
    assert solution.bestCoordinate(
        towers=[[1, 2, 5], [2, 1, 7], [3, 1, 9]], radius=2
    ) == [2, 1]
    assert solution.bestCoordinate(towers=[[23, 11, 21]], radius=9) == [23, 11]
    assert solution.bestCoordinate(
        towers=[[1, 2, 13], [2, 1, 7], [0, 1, 9]], radius=2
    ) == [1, 2]
    """
    assert solution.bestCoordinate(towers=[[2, 1, 9], [0, 1, 9]], radius=2) == [0, 1]


def test_1637():
    from .lc_1637 import Solution

    solution = Solution()
    solution.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]) == 1
    solution.maxWidthOfVerticalArea(
        [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    ) == 3


def test_1647():
    from .lc_1647 import Solution

    solution = Solution()
    assert solution.minDeletions("aab") == 0
    assert solution.minDeletions("aaabbbcc") == 2
    assert solution.minDeletions("ceabaacb") == 2
    assert solution.minDeletions("bbcebab") == 2


def test_1652():
    from .lc_1652 import Solution

    solution = Solution()
    assert solution.decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
    assert solution.decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
    assert solution.decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
