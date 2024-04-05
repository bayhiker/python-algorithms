class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        return self.longest_ideal_string_dp_26(s, k)

    def longest_ideal_string_dp_26(self, s: str, k: int) -> int:
        """
        dp[i]: length of longest ideal subsequence that ends with char[org[a] + i]
        """
        ord_a = ord("a")
        dp: list[int] = [0] * 26
        for c in s:
            curr_letter_index = ord(c) - ord("a")
            curr_max = dp[curr_letter_index]
            for j in range(curr_letter_index - k, curr_letter_index + k + 1):
                if j < 0 or j > 25:
                    continue
                curr_max = max(curr_max, 1 + dp[j])
            dp[curr_letter_index] = curr_max
        return max(dp)

    def longest_ideal_string_dp_n(self, s: str, k: int) -> int:
        """dp[i] length of longest ideal subsequence that ends with s[i]

        Args:
            s (str): _description_
            k (int): _description_

        Returns:
            int: _description_
        """
        n = len(s)
        dp = [1] * n
        overall_max = 1
        for i in range(1, n):
            curr_max = dp[i]
            for j in range(i):
                if abs(ord(s[j]) - ord(s[i])) <= k:
                    if dp[j] + 1 > curr_max:
                        curr_max = dp[j] + 1
            dp[i] = curr_max
            if curr_max > overall_max:
                overall_max = curr_max
        return overall_max
