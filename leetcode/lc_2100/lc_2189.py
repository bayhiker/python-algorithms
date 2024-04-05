class Solution:
    def houseOfCards(self, n: int) -> int:
        return self.house_of_cards(n)

    def house_of_cards(self, n: int) -> int:
        # Observation: If a layer has x houses, then it uses 3*x - 1 cards
        # dp[0] = 1
        # dp[i] = sum(dp[i - used_cards])
        #         where usedCards = 3 * x - 1, 0<=x<=i/3
        pass
