# leetcode_877_1140_1406_1510_1563_1686_1690_1872_2029

# Stone Game i:
# Given a row of piles of stones, each pile contains piles[i] stones.
# Alice and Bob take turns taking a pile of stones from either end.
# Alice goes first. At the end of the game, whoever gets the most
# stones wins the game.
#
# Assumptions:
# - 2 < len(piles) < 500
# - len(piles) is even
# - sum(piles) is odd, so no ties
# - Both players are logical and smart
#


# leetcode_877
def wins_stone_game_i(piles):
    return True


# Stone Game ii:
# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
# On each player's turn, that player can take all the stones in the first
# X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
# The game continues until all the stones have been taken.
# Find the max number of stones Alice can get
#
# Assumptions:
# - 1 <= piles[i] <= 10000
# - 1 <= len(piles) <= 100
def max_stones_dp(piles):
    pass
