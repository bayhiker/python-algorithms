class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low_odd = low % 2
        high_odd = high % 2
        diff = high - low + (1 if low_odd else 0) + (1 if high_odd else 0)
        return int(diff / 2)
