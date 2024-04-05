from .number import factorize


def test_factorize():
    assert factorize(2) == {2: 1}
    assert factorize(8) == {2: 3}
    assert factorize(300) == {2: 2, 3: 1, 5: 2}
    assert factorize(6008) == {2: 3, 751: 1}
    assert factorize(600860086008) == {2: 3, 3: 1, 7: 1, 13: 1, 37: 1, 751: 1, 9901: 1}
    assert factorize(1234567890000000000) == {2: 10, 3: 2, 5: 10, 3607: 1, 3803: 1}
    assert factorize(10**100) == {2: 100, 5: 100}
    assert factorize(1) is None
    assert factorize(0) is None
    assert factorize(-10) is None
