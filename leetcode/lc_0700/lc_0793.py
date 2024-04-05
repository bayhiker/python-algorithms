class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        return self.pre_image_size_fzf(k)

    def preimage_size_fzf(self, k: int) -> int:
        # - 0 in x! can only be generated with 2s and 5s
        # - prime factorize all numbers, and check the number of (2,5) pairs
        # - For any x, 2 factors are always more plentiful, so only count 5s
        # - k is rather large: 10**9, watch out for TLE
        # - f(x) is non-decreasing, possibly use BINARY SEARCH
        pass

    @staticmethod
    def get_trailing_zeroes(x: int):
        # Get number of trailing zeros for x!
        zeroes = 0
        while x > 0:
            x //= 5
            zeroes += x
        return zeroes
