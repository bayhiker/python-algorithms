class Solution:
    def minOperations(self, n: int) -> int:
        return self.min_operations(n)

    def min_operations(self, n: int) -> int:
        # Observation 1: starting from two ends 1 and 2n-1, sub/add n-1, then move inwards
        # Observation 2: when n is odd, there are 2 + 4 + 6 + ... + (n-1) ops
        # Observation 3: when n is even, there are 1 + 3 + 5 + ... + (n-1) ops``
        return (n * n - (1 if n % 2 else 0)) // 4
