def test_0842():
    from .lc_0842 import Solution

    solution = Solution()
    assert solution.splitIntoFibonacci("123456579") == [123, 456, 579]
    assert solution.splitIntoFibonacci("1101111") == [11, 0, 11, 11]
    assert solution.splitIntoFibonacci("112358130") == []
    assert solution.splitIntoFibonacci("0123") == []
    assert solution.splitIntoFibonacci("0000") == [0, 0, 0, 0]
    assert (
        solution.splitIntoFibonacci(
            "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
        )
        == []
    )  # All numbers should be less than 2**31
    assert solution.splitIntoFibonacci("1023") == []


def test_0842():
    from .lc_0892 import Solution

    solution = Solution()
    assert solution.surfaceArea([[1, 2], [3, 4]]) == 34
    assert solution.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 32
    assert solution.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]) == 46
