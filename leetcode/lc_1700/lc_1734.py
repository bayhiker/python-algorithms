class Solution:
    def decode(self, encoded: list[int]) -> list[int]:
        # Observation:
        # permutation 1-n, xor'ed together is 1 if n=4x+1, 0 if n=4x+3,
        # therefore, and we know a2^a3, a4^a5, ...., thereby we can get a1
        n = len(encoded) + 1
        result = [0 for _ in range(n)]
        if n % 4 == 1:
            result[0] = 1
        for i in range(n - 1):
            if i % 2:
                result[0] ^= encoded[i]
        for i in range(n - 1):
            result[i + 1] = result[i] ^ encoded[i]
        return result
