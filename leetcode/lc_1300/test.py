def test_1324():
    from .lc_1324 import Solution

    solution: Solution = Solution()
    assert solution.printVertically("HOW ARE YOU") == ["HAY", "ORO", "WEU"]
    assert solution.printVertically("TO BE OR NOT TO BE") == [
        "TBONTB",
        "OEROOE",
        "   T",
    ]
    assert solution.printVertically("CONTEST IS COMING") == [
        "CIC",
        "OSO",
        "N M",
        "T I",
        "E N",
        "S G",
        "T",
    ]


def test_1347():
    from .lc_1347 import Solution

    solution: Solution = Solution()
    assert solution.minSteps("bab", "aba") == 1
    assert solution.minSteps("leetcode", "practice") == 5


def test_1375():
    from .lc_1375 import Solution

    solution: Solution = Solution()
    assert solution.numTimesAllBlue([3, 2, 4, 1, 5]) == 2
    assert solution.numTimesAllBlue(flips=[4, 1, 2, 3]) == 1
