class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        """
        Problem constraint has n >= 4
        If n > 5, base n-2 of the number is always x2 where x is not 2, return false
        If n is 4, base 2 is 100, return false
        """
        return False
