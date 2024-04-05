def test_0632() -> None:
    from .lc_0632 import Solution

    solution = Solution()
    assert solution.smallestRange(
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    ) == [20, 24]
    assert solution.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [1, 1]


def test_0665():
    from .lc_0665 import Solution

    solution = Solution()
    assert solution.checkPossibility(nums=[4, 2, 3]) is True
    assert solution.checkPossibility(nums=[4, 2, 1]) is False
    assert solution.checkPossibility(nums=[3, 4, 2, 3]) is False


def test_0673():
    from .lc_0673 import Solution

    solution = Solution()
    assert solution.findNumberOfLIS([1, 3, 5, 4, 7]) == 2
    assert solution.findNumberOfLIS([2, 2, 2, 2, 2]) == 5


def test_0676():
    from .lc_0676 import MagicDictionary

    magic_dict = MagicDictionary()
    magic_dict.buildDict(["hello", "leetcode"])
    assert magic_dict.search("hello") is False
    assert magic_dict.search("hhllo") is True
    assert magic_dict.search("hell") is False
    assert magic_dict.search("leetcoded") is False


def test_0678():
    from .lc_0678 import Solution

    solution = Solution()
    assert solution.checkValidString("()") is True
    assert solution.checkValidString("(*)") is True
    assert solution.checkValidString("(*))") is True
    assert solution.checkValidString("(((((*))") is False


def test_0693():
    from .lc_0693 import Solution

    solution = Solution()
    assert solution.hasAlternatingBits(5) is True
    assert solution.hasAlternatingBits(7) is False
    assert solution.hasAlternatingBits(11) is False


def test_0697():
    from .lc_0697 import Solution

    solution = Solution()
    assert solution.findShortestSubArray([1, 2, 2, 3, 1]) == 2
    assert solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6
