from .tree import array2bt, bt2array


def test_array_bt():
    root = [2, 3, 1, 3, 1, None, 1]
    assert bt2array(array2bt(root)) == root
