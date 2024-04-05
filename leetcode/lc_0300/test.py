def test_0328():
    from .lc_0328 import Solution, get_linked_list, get_list

    solution: Solution = Solution()

    assert get_list(solution.oddEvenList(get_linked_list([1, 2, 3, 4, 5]))) == [
        1,
        3,
        5,
        2,
        4,
    ]

    assert get_list(solution.oddEvenList(get_linked_list([2, 1, 3, 5, 6, 4, 7]))) == [
        2,
        3,
        6,
        7,
        1,
        5,
        4,
    ]


def test_0358():
    from .lc_0358 import Solution

    solution = Solution()
    """
    s = solution.rearrangeString("aabbcc", 3)
    assert (
        s == "abcabc"
        or s == "acbacb"
        or s == "bacbac"
        or s == "bcabca"
        or s == "cabcab"
        or s == "cbacba"
    )
    assert solution.rearrangeString("aaabc", 3) == ""
    """
    assert solution.rearrangeString("aaadbbcc", 2) == "abacabcd"
