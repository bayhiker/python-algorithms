from bisect import bisect, bisect_left, bisect_right


def bs_bisect(a, x):
    ins_point = bisect_left(a, x)
    if ins_point != len(a) and a[ins_point] == x:
        return ins_point
    else:
        return -1


def test_bs_bisect():
    a0 = []
    a1 = [1]
    a5 = [1, 3, 5, 7, 9]
    a6 = [1, 3, 5, 7, 9, 11]
    assert bs_bisect(a0, 3) == -1
    assert bs_bisect(a1, 1) == 0
    assert bs_bisect(a1, 3) == -1
    assert bs_bisect(a5, 3) == 1
    assert bs_bisect(a5, 4) == -1
    assert bs_bisect(a6, 3) == 1
    assert bs_bisect(a6, 4) == -1
    assert bs_bisect(a6, 1) == 0
    assert bs_bisect(a6, 11) == 5
