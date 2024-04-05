from lib.singly_linked_list import get_linked_list, get_list


def test_2007():
    from .lc_2007 import Solution

    solution = Solution()
    # assert solution.findOriginalArray(changed=[1, 3, 4, 2, 6, 8]) == [1, 3, 4]
    assert solution.findOriginalArray(changed=[6, 3, 0, 1]) == []


def test_2028():
    from .lc_2028 import Solution

    solution = Solution()
    assert sum(solution.missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2)) == sum([6, 6])
    assert sum(solution.missingRolls(rolls=[1, 5, 6], mean=3, n=4)) == sum([2, 3, 2, 2])
    assert solution.missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4) == []

def test_2035():
    from .lc_2035 import Solution

    solution = Solution()
    assert solution.minimumDifference([3,9,7,3]) == 2
    assert solution.minimumDifference([-36, 36]) == 72
    assert solution.minimumDifference([2,-1,0,4,-2,-9]) == 0
    assert solution.minimumDifference([0,6,11,17,18,24]) == 6
    assert solution.minimumDifference([7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]) == 1

def test_2058():
    from .lc_2058 import Solution

    solution = Solution()
    head = get_linked_list([5, 3, 1, 2, 5, 1, 2])
    assert solution.nodesBetweenCriticalPoints(head) == [1, 3]
    head = get_linked_list([1, 3, 2, 2, 3, 2, 2, 2, 7])
    assert solution.nodesBetweenCriticalPoints(head) == [3, 3]


def test_2061():
    from .lc_2061 import Solution

    solution: Solution = Solution()
    assert solution.numberOfCleanRooms([[0, 0, 0], [1, 1, 0], [0, 0, 0]]) == 7
    assert solution.numberOfCleanRooms([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) == 1


def test_2075():
    from .lc_2075 import Solution
    from .testdata_2975 import encoded_text, plain_text

    solution = Solution()
    # assert solution.decodeCiphertext("ch   ie   pr", 3) == "cipher"
    # assert solution.decodeCiphertext("iveo    eed   l te   olc", 4) == "i love leetcode"
    # assert solution.decodeCiphertext("coding", 1) == "coding"
    # assert solution.decodeCiphertext("", 5) == ""
    # assert solution.decodeCiphertext("a ", 2) == "a"
    assert solution.decodeCiphertext(encoded_text, 1000) == plain_text
