class Solution:
    def canWinNim(self, n: int) -> bool:
        return self.can_win_nim(n)

    def can_win_nim(self, n: int) -> bool:
        return not n % 4 == 0
