from collections import deque


class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.check_valid_string(s)

    def check_valid_string(self, s: str) -> bool:
        lo, hi = 0, 0  # Lower and upper bound for potential extra left parentheses
        for c in s:
            if c == "(":
                lo += 1
                hi += 1
            elif c == ")":
                lo -= 1
                hi -= 1
            else:  # c is *
                lo -= 1
                hi += 1
            if hi < 0:
                break
            lo = max(lo, 0)
        return lo <= 0 and hi >= 0
