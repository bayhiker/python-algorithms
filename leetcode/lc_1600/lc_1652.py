class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        if k < 0:
            code = code[n + k : n] + code
            k_sum = sum(code[n - 1 : n - k - 1])
            for i in range(n - k - 1, -k - 1, -1):
                code[i] = k_sum
                k_sum = k_sum - code[i - 1] + code[i - 1 + k]
            return code[-k : n - k]
        if k > 0:
            code = code + code[0 : k + 1]
            k_sum = sum(code[1 : k + 1])
            for i in range(n):
                code[i] = k_sum
                k_sum = k_sum - code[i + 1] + code[i + 1 + k]
            return code[0:n]
