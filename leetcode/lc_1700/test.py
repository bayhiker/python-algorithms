def test_lc1721():
    from .lc_1721 import Solution
    from lib.singly_linked_list import get_list, get_linked_list

    solution = Solution()
    # assert get_list(solution.swapNodes(get_linked_list([1]), 1)) == [1]
    # assert get_list(solution.swapNodes(get_linked_list([1, 2]), 1)) == [2, 1]
    assert get_list(
        solution.swapNodes(
            get_linked_list(
                [100, 24, 24, 36, 18, 52, 95, 61, 54, 88, 86, 79, 11, 1, 31, 26]
            ),
            16,
        )
    ) == [26, 24, 24, 36, 18, 52, 95, 61, 54, 88, 86, 79, 11, 1, 31, 100]
    """ 
    assert get_list(solution.swapNodes(get_linked_list([80, 46, 66, 35, 64]), 1)) == [
        64,
        46,
        66,
        35,
        80,
    ]
    assert get_list(solution.swapNodes(get_linked_list([1, 2, 3, 4, 5]), 2)) == [
        1,
        4,
        3,
        2,
        5,
    ]

    assert get_list(
        solution.swapNodes(get_linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5)
    ) == [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
    """


def test_1734():
    from .lc_1734 import Solution

    solution = Solution()
    assert solution.decode([3, 1]) == [1, 2, 3]
    assert solution.decode([6, 5, 4, 6]) == [2, 4, 1, 5, 3]


def test_1765():
    from .lc_1765 import Solution

    def max2d(matrix) -> int:
        return max(map(max, matrix))

    solution = Solution()
    assert max2d(solution.highestPeak([[0, 1], [0, 0]])) == 2
    assert max2d(solution.highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]])) == 2


def test_1798():
    from .lc_1798 import Solution

    solution = Solution()
    assert solution.getMaximumConsecutive([1, 3]) == 2
    assert solution.getMaximumConsecutive([1, 1, 1, 4]) == 8
    assert solution.getMaximumConsecutive([1, 4, 10, 3, 1]) == 20
