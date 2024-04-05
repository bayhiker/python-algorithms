from pytest import mark


def test_2671():
    from .lc_2671 import Solution

    solution = Solution()


def test_2646():
    from .lc_2646 import Solution

    solution = Solution()
    assert (
        solution.minimumTotalPrice(
            n=4,
            edges=[[0, 1], [1, 2], [1, 3]],
            price=[2, 2, 10, 6],
            trips=[[0, 3], [2, 1], [2, 3]],
        )
        == 23
    )
