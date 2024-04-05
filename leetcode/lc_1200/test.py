def test_1247():
    from .lc_1247 import Solution

    solution = Solution()
    assert solution.minimumSwap("xx", "yy") == 1
    assert solution.minimumSwap("xy", "yx") == 2
    assert solution.minimumSwap("xx", "xy") == -1


def test_1276():
    from .lc_1276 import Solution

    solution: Solution = Solution()
    assert solution.numOfBurgers(16, 7) == [1, 6]
    assert solution.numOfBurgers(17, 4) == []
    assert solution.numOfBurgers(4, 17) == []


def test_1296():
    from .lc_1296 import Solution

    solution: Solution = Solution()
    assert solution.isPossibleDivide( nums = [1,2,3,3,4,4,5,6], k = 4) is True
    assert solution.isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], k = 3) is True
    assert solution.isPossibleDivide([1,2,3,4], 3) is False
