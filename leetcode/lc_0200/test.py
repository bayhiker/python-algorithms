def test_0214():
    from .lc_0214 import Solution

    solution: Solution = Solution()
    assert solution.shortestPalindrome("abcd") == "dcbabcd"
    assert solution.shortestPalindrome("aacecaaa") == "aaacecaaa"
    assert solution.shortestPalindrome("abbacd") == "dcabbacd"
    assert solution.shortestPalindrome("babbbabbaba") == "ababbabbbabbaba"
