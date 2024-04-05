def test_1815():
    from .lc_1815 import Solution

    solution: Solution = Solution()
    """
    assert solution.maxHappyGroups(3, [1, 2, 3, 4, 5, 6]) == 4
    assert solution.maxHappyGroups(4, [1, 3, 2, 5, 2, 2, 1, 6]) == 4
    assert (
        solution.maxHappyGroups(
            3,
            [
                484091167,
                239654641,
                562528444,
                696328470,
                32964170,
                424018512,
                724671126,
                618309892,
                862628625,
            ],
        )
        == 6
    )
    assert (
        solution.maxHappyGroups(
            7,
            [
                145326640,
                622724151,
                591814792,
                827053040,
                111964428,
                344376875,
                42023891,
                436582274,
                78590835,
                408269112,
                930041188,
                846233596,
                158192647,
                889601516,
                134236253,
                366035866,
                123146762,
            ],
        )
        == 9
    )
    """
    assert (
        solution.maxHappyGroups(
            7,
            [
                2,
                7,
                5,
                2,
                3,
                2,
                6,
                5,
                3,
                6,
                2,
                3,
                7,
                2,
                2,
                5,
                4,
                6,
                6,
                4,
                7,
                5,
                6,
                1,
                6,
                2,
                6,
                6,
                2,
                5,
            ],
        )
        == 15
    )


def test_1835():
    from .lc_1835 import Solution

    solution = Solution()
    assert solution.getXORSum([1, 2, 3], [6, 5]) == 0
    assert solution.getXORSum(arr1=[12], arr2=[4]) == 4
    assert (
        solution.getXORSum(
            arr1=[416], arr2=[150, 6245, 3548, 6915, 475, 8644, 3632, 7174, 8123]
        )
        == 416
    )


def test_1889():
    from .lc_1889 import Solution

    solution = Solution()
    """ 
    assert solution.minWastedSpace(packages=[2, 3, 5], boxes=[[4, 8], [2, 8]]) == 6
    assert solution.minWastedSpace([2, 3, 5], [[1, 4], [2, 3], [3, 4]]) == -1
    assert (
        solution.minWastedSpace([3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]])
        == 9
    )
    """
    assert (
        solution.minWastedSpace(packages=[7, 6, 5, 3, 4], boxes=[[2, 7], [6], [10, 5]])
        == 10
    )


def test_1894():
    from .lc_1894 import Solution

    solution = Solution()
    assert solution.chalkReplacer(chalk=[5, 1, 5], k=22) == 0
    assert solution.chalkReplacer(chalk=[3, 4, 1, 2], k=25) == 1
