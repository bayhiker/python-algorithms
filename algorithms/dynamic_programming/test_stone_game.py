from .stone_game import (
    stone_game_ii_dp,
    stone_game_iii_dp,
    stone_game_iv_dp,
    stone_game_ix_counting,
    stone_game_v_dp,
    stone_game_vi_greedy,
    stone_game_vii_dp_memoization,
    stone_game_vii_dp_tabulation,
    stone_game_viii_dp,
)


def test_stone_game_ii():
    assert stone_game_ii_dp([2, 7, 9, 4, 4]) == 10


def test_stone_game_iii():
    assert stone_game_iii_dp([1]) == "Alice"
    assert stone_game_iii_dp([1, 2, 3, 7]) == "Bob"
    assert stone_game_iii_dp([1, 2, 3, -9]) == "Alice"
    assert stone_game_iii_dp([1, 2, 3, 6]) == "Tie"


def test_stone_game_iv():
    assert stone_game_iv_dp(1)
    assert not stone_game_iv_dp(2)
    assert stone_game_iv_dp(100)
    assert not stone_game_iv_dp(7)
    assert not stone_game_iv_dp(17)


def test_stone_game_v():
    assert stone_game_v_dp([6, 2, 3, 4, 5, 5]) == 18
    assert stone_game_v_dp([7, 7, 7, 7, 7, 7, 7]) == 28
    assert stone_game_v_dp([98, 77, 24, 49, 6, 12, 2, 44, 51, 96]) == 330
    # stoneValues = [776886] * 500
    # assert stone_game_v_dp(stoneValues) == 383781684


def test_stone_game_vi():
    assert stone_game_vi_greedy([1, 3], [2, 1]) == 1
    assert stone_game_vi_greedy([1, 2], [3, 1]) == 0


def test_stone_game_vii_dp_memoization():
    assert stone_game_vii_dp_memoization([5, 3]) == 5
    assert stone_game_vii_dp_memoization([5, 5, 5, 5]) == 10
    assert stone_game_vii_dp_memoization([5, 5, 5, 5, 5]) == 10
    assert stone_game_vii_dp_memoization([5, 3, 1, 4, 2]) == 6
    assert stone_game_vii_dp_memoization([7, 90, 5, 1, 100, 10, 10, 2]) == 122


def test_stone_game_vii_dp_tabulation():
    assert stone_game_vii_dp_tabulation([5, 3]) == 5
    assert stone_game_vii_dp_tabulation([5, 5, 5, 5]) == 10
    assert stone_game_vii_dp_tabulation([5, 5, 5, 5, 5]) == 10
    assert stone_game_vii_dp_tabulation([5, 3, 1, 4, 2]) == 6
    assert stone_game_vii_dp_tabulation([7, 90, 5, 1, 100, 10, 10, 2]) == 122


def test_stone_game_viii_dp():
    assert stone_game_viii_dp([2, 2]) == 4
    assert stone_game_viii_dp([-2, -2]) == -4
    assert stone_game_viii_dp([-1, 2, -3, 4, -5]) == 5


def test_stone_game_ix_counting():
    assert stone_game_ix_counting([2, 1])
    assert not stone_game_ix_counting([2])
    assert not stone_game_ix_counting([5, 1, 2, 4, 3])
    assert not stone_game_ix_counting([2, 3])
    assert stone_game_ix_counting([20, 3, 20, 17, 2, 12, 15, 17, 4])
    assert not stone_game_ix_counting([10000] * 100000)
