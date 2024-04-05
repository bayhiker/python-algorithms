class Solution:
    def binaryGap(self, n: int) -> int:
        return self.binary_gap(n)

    def binary_gap(self, n: int) -> int:
        # n % 2 is the last bit of n
        # Use binary shift right to check bit by bit, record distance between 1s along the way
        pass
