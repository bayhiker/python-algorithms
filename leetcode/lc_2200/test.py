def test_2237():
    from .lc_2233 import Solution

    solution: Solution = Solution()
    assert solution.maximumProduct([0, 4], 5) == 20
    assert solution.maximumProduct(nums=[6, 3, 3, 2], k=2) == 216
