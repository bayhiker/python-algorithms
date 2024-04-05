from .kmp import get_table, kmp_search


def test_get_table():
    assert get_table("abcdabd") == [0, 0, 0, 0, 1, 2, 0]
    assert get_table("aaaa") == [0,1,2,3]
    assert get_table("ABCD") == [0,0,0,0]
    assert get_table("AABAACAABAA") == [0,1,0,1, 2,0,1,2,3,4, 5]
    assert get_table("AAACAAAAAC") == [0,1,2,0, 1,2,3,3,3,4]
    assert get_table("babbbabbaba") == [0,0,1,1,1,2,3,4,2,3,2]


def test_kmp_search():
    assert kmp_search("aabcdababcdabdabcdababcdabd", "abcdabd") == [7, 20]
    assert kmp_search("AABAACAADAABAAABAA", "AABA") == [0, 9, 13]
