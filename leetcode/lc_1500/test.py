def test_1520():
    from .lc_1520 import Solution

    solution = Solution()
    assert solution.maxNumOfSubstrings("adefaddaccc") == ["e", "f", "ccc"]
    assert solution.maxNumOfSubstrings("abbaccd") == ["bb", "cc", "d"]
    assert solution.maxNumOfSubstrings("abab") == ["abab"]
    assert solution.maxNumOfSubstrings("ababa") == ["ababa"]
    assert sorted(solution.maxNumOfSubstrings("badadbeabc")) == sorted(["c", "e"])


def test_1523():
    from .lc_1523 import Solution

    solution = Solution()
    assert solution.countOdds(3, 7) == 3


def test_1551():
    from .lc_1551 import Solution

    solution = Solution()
    assert solution.minOperations(3) == 2
    assert solution.minOperations(6) == 9


def test_1560():
    from .lc_1560 import Solution

    s = Solution()
    assert s.mostVisited(n=4, rounds=[1, 3, 1, 2]) == [1, 2]
    assert s.mostVisited(n=2, rounds=[2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2]
    assert s.mostVisited(n=3, rounds=[3, 2, 1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 3, 1]) == [
        1,
        3,
    ]


def test_1573():
    from .lc_1573 import Solution

    solution = Solution()
    assert solution.numWays("10101") == 4
    assert solution.numWays("1001") == 0
    assert solution.numWays("0000") == 3


def test_1598():
    from .lc_1598 import Solution

    solution = Solution()
    assert solution.minOperations(["d1/", "d2/", "../", "d21/", "./"]) == 2
    assert solution.minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]) == 3
    assert solution.minOperations(["d1/", "../", "../", "../"]) == 0
