from lib.tree import array2bt, bt2array


def test_1457():
    from .lc_1457 import Solution

    solution = Solution()
    assert solution.pseudoPalindromicPaths(array2bt([2, 3, 1, 3, 1, None, 1])) == 2
    root = [2, 1, 1, 1, 3, None, None, None, None, None, 1]
    assert solution.pseudoPalindromicPaths(array2bt(root)) == 1
    assert solution.pseudoPalindromicPaths(array2bt([9])) == 1


def test_1461():
    from .lc_1461 import Solution

    solution = Solution()
    # assert solution.hasAllCodes(s="00110110", k=2) is True
    # assert solution.hasAllCodes(s="0110", k=1) is True
    # assert solution.hasAllCodes(s="0110", k=2) is False
    assert solution.hasAllCodes(s="0000000001011100", k=4) is False


def test_1465() -> None:
    from .lc_1465 import Solution

    solution = Solution()
    assert (
        solution.maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]) == 4
    )
    assert solution.maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]) == 6
    assert solution.maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]) == 9


def test_1473():
    from .lc_1473 import Solution

    solution: Solution = Solution()
    assert (
        solution.minCost(
            houses=[0, 0, 0, 0, 0],
            cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
            m=5,
            n=2,
            target=3,
        )
        == 9
    )

    assert (
        solution.minCost(
            houses=[0, 2, 1, 2, 0],
            cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
            m=5,
            n=2,
            target=3,
        )
        == 11
    )

    assert (
        solution.minCost(
            houses=[3, 1, 2, 3],
            cost=[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
            m=4,
            n=3,
            target=3,
        )
        == -1
    )
