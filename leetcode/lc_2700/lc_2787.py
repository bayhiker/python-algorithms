from math import log, e, ceil
from functools import lru_cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # max possible base b is  b** x <= n, and (b+1) ** x > n
        return self.number_of_ways(n, x, ceil(e ** (log(n) / x)))

    @lru_cache
    def number_of_ways(self, n: int, x: int, current_base) -> int:
        # TLE
        if current_base**x == n:
            return 1 + self.number_of_ways(n, x, current_base - 1)
        if current_base < 1 or n < 1:
            return 0
        return (
            self.number_of_ways(n, x, current_base - 1)
            + self.number_of_ways(n - current_base**x, x, current_base - 1)
        ) % (10**9 + 7)
