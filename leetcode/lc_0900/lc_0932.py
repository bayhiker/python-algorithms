class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        return self.beautiful_array(n)

    def beautiful_array(self, n: int) -> list[int]:
        memo = {1: [1]}

        def f(n):
            if n not in memo:
                odds = f((n + 1) // 2)
                evens = f(n // 2)
                memo[n] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
            return memo[n]

        return f(n)
