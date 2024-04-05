class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        return self.get_xor_sum(arr1, arr2)

    def get_xor_sum(self, arr1: list[int], arr2: list[int]) -> int:
        # Observation 1: & changes both bits to 0 unless two 1s
        # Observation 2: ^ tests parity of number of 1s and 0s at i'th bit
        # Instead of going through all numbers O(m*n), this problem can be solved
        # by studying the bits in arr1 and arr2 and potentially be solved in O(m+n)
        #

        m, n = len(arr1), len(arr2)
        # First 32 stores num of 1bits in nums in arr1, last 32 for arr2
        one_bits = [0] * 64
        for i, num in enumerate(arr1 + arr2):
            bit_no = int(i >= m) * 32
            while num > 0:
                one_bits[bit_no] += num % 2
                num = num >> 1
                bit_no += 1
        # One bits in m*n numbers from bitwise_and is
        #    one_bits_original[i] * one_bits_original[i + 32] for i in range(32)
        power = 1
        xor_sum = 0
        for i in range(32):
            xor_sum += power * int(
                one_bits[i] % 2 == 1 and one_bits[i + 32] % 2 == 1
            )  # xor result of that bit is 1 if and only if there are even number of 1s on that bit
            power *= 2
        return xor_sum
