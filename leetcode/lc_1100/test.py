def test_1104():
    from .lc_1104 import Solution

    solution = Solution()
    assert solution.pathInZigZagTree(14) == [1, 3, 4, 14]
    assert solution.pathInZigZagTree(26) == [1, 2, 6, 10, 26]


def test_1147():
    from .lc_1147 import Solution

    solution = Solution()
    text = "ghiabcdefhelloadamhelloabcdefghi"
    assert solution.longestDecomposition(text) == 7
    assert solution.longestDecomposition("merchant") == 1
    text = "antaprezatepzapreanta"
    assert solution.longestDecomposition(text) == 11
