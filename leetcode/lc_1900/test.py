def test_1916():
    from .lc_1916 import Solution

    solution: Solution = Solution()
    assert solution.waysToBuildRooms(prevRoom=[-1, 0, 1]) == 1
    assert solution.waysToBuildRooms(prevRoom=[-1, 0, 0, 1, 2]) == 6


def test_1922():
    from .lc_1922 import Solution

    solution: Solution = Solution()
    assert solution.countGoodNumbers(1) == 5
    assert solution.countGoodNumbers(4) == 400
    assert solution.countGoodNumbers(50) == 564908303
    assert solution.countGoodNumbers(806166225460393) == 643535977


def test_1943():
    from .lc_1943 import Solution

    s = Solution()
    assert s.splitPainting(segments=[[1, 4, 5], [4, 7, 7], [1, 7, 9]]) == [
        [1, 4, 14],
        [4, 7, 16],
    ]


def test_1980():
    from .lc_1980 import Solution

    solution = Solution()
    # assert solution.findDifferentBinaryString(nums=["01", "10"]) == "00"
    assert (
        solution.findDifferentBinaryString(
            [
                "0000000111",
                "0000001001",
                "0000000100",
                "0000000001",
                "0000000010",
                "1111111111",
                "0000000101",
                "0000000000",
                "0000001000",
                "0000000110",
            ]
        )
        == "0000000011"
    )
