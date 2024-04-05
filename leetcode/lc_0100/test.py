def test_0115():
    from .lc_0115 import Solution

    solution: Solution = Solution()
    # assert solution.numDistinct("rabbbit", "rabbit") == 3
    assert solution.numDistinct("babgbag", "bag") == 5


def test_0119():
    from .lc_0119 import Solution

    solution: Solution = Solution()
    assert solution.getRow(0) == [1]
    assert solution.getRow(1) == [1, 1]
    assert solution.getRow(3) == [1, 3, 3, 1]
    assert solution.getRow(6) == [1, 6, 15, 20, 15, 6, 1]
