def test_2462():
    from .lc_2462 import Solution

    solution: Solution = Solution()
    assert solution.totalCost() == 4


def test_2463():
    from .lc_2463 import Solution

    solution: Solution = Solution()
    assert solution.minimumTotalDistance(robot=[0, 4, 6], factory=[[2, 2], [6, 2]]) == 4
    assert solution.minimumTotalDistance(robot=[1, -1], factory=[[-2, 1], [2, 1]]) == 2
