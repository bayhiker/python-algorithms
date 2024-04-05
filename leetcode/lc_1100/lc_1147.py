class Solution:
    def longestDecomposition(self, text: str) -> int:
        return self.longest_decomposition(text)

    def longest_decomposition(self, text: str) -> int:
        # Greedy
        n, start, result = len(text), 0, 0
        for i in range(n // 2):
            candidate = text[start : i + 1]
            if candidate == text[n - i - 1 : n - start]:
                result += 1
                start = i + 1
        return result * 2 + (1 if n % 2 or start < n // 2 else 0)
