class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Count all characters, at most 1 char can appear odd number of times
        # A one liner solution is: return sum(v % 2 for v in Counter(s).values()) <= 1
        pass
