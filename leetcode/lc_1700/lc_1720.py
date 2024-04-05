from itertools import accumulate
from operator import xor

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        return self.decode_accumulate(encoded, first)

    def decode_accumulate(self, encoded: list[int], first: int) -> list[int]:
        return accumulate(encoded, xor, initial=first)
        
    def decode_loop(self, encoded: list[int], first: int) -> list[int]:
        decoded: list[int] = [first]
        for i in range(len(encoded)):
            decoded.append(decoded[i] ^ encoded[i])
        return decoded

