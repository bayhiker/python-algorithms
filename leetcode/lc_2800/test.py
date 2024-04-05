from pytest import mark


# @mark.skip
def test_2818():
    from .lc_2818 import Solution

    solution = Solution()
    assert solution.maximumScore([8, 3, 9, 3, 8], 2) == 81
    assert solution.maximumScore(nums=[19, 12, 14, 6, 10, 18], k=3) == 4788
    assert solution.maximumScore([3289, 2832, 14858, 22011], 6) == 256720975


def test_2875():
    from .lc_2875 import Solution

    solution = Solution()
    assert solution.minSizeSubarray([1, 2, 3], 5) == 2
    assert solution.minSizeSubarray([1, 1, 1, 2, 3], 4) == 2
    assert solution.minSizeSubarray([2, 4, 6, 8], 3) == -1
    assert solution.minSizeSubarray([1, 11, 6, 4, 13], 22) == 4
