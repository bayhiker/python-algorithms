def test_2762():
    from .lc_2762 import Solution

    solution: Solution = Solution()
    assert solution.continuousSubarrays(nums=[5, 4, 2, 4]) == 8
    assert solution.continuousSubarrays(nums=[1, 2, 3]) == 6


def test_2787():
    from .lc_2787 import Solution

    solution: Solution = Solution()
    assert solution.numberOfWays(10, 2) == 1
    assert solution.numberOfWays(n=4, x=1) == 2
