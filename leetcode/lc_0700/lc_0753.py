class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        return self.crack_safe(n, k)

    def crack_safe(self, n: int, k: int) -> str:
        # Observation: There are totally k**n possible codes,
        # Min length code is of length k**n + n - 1, where every code reuses the
        # last (n-1) digits from the previous code
        #
        # Use DFS to traverse each node once and only once (Euler path)
        pass
