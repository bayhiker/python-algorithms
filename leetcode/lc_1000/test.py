def test_1014():
    from .lc_1014 import Solution

    solution = Solution()
    assert solution.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
    assert solution.maxScoreSightseeingPair([1, 2]) == 2
