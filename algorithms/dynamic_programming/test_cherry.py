from typing import List
from .cherry import cherry_pickup_i_dp, cherry_pickup_ii_dp


def test_cherry_pickup_i_dp():
    assert cherry_pickup_i_dp([[0, 1, -1], [1, 0, -1], [1, 1, 1]]) == 5
    assert cherry_pickup_i_dp([[1, 1, -1], [1, -1, 1], [-1, 1, 1]]) == 0


def test_cherry_pickup_ii_dp():
    assert (
        cherry_pickup_ii_dp([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]])
        == 22
    )
    assert cherry_pickup_ii_dp([[1, 1], [1, 1]]) == 4
