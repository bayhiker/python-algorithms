def test_2137():
    from .lc_2137 import Solution

    solution: Solution = Solution()
    assert solution.equalizeWater(buckets=[1, 2, 7], loss=80) == 2
    assert solution.equalizeWater(buckets=[2, 4, 6], loss=50) == 3.5
    assert solution.equalizeWater(buckets=[3, 3, 3, 3], loss=40) == 3


def test_2169():
    from .lc_2169 import Solution

    solution: Solution = Solution()
    assert solution.countOperations(2, 3) == 3
    assert solution.countOperations(10, 10) == 1


def test_2176():
    from .lc_2176 import Solution

    solution = Solution()
    assert solution.countPairs(nums=[3, 1, 2, 2, 2, 1, 3], k=2) == 4
    assert solution.countPairs(nums=[1, 2, 3, 4], k=1) == 0


def test_2177():
    from .lc_2177 import Solution

    solution: Solution = Solution()
    assert solution.sumOfThree(33) == [10, 11, 12]
    assert solution.sumOfThree(4) == []
