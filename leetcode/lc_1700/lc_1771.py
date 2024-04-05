class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        return self.longest_palindrome(word1, word2)

    def longest_palindrome(self, word1: str, word2: str) -> int:
        # word = word1 + word2
        # n, n1, n2 = len(word), len(word1), len(word2)
        # dp[i][j]: longest palindromic subsequence in word[i:j+1]
        # dp[i-1][j+1] = 2 + dp[i][j] if word[i-1] == word[j+1] else max(dp[i][j+1], dp[i-1][j])
        # dp[0, len(w)] is not the answer, need to make sure first letter is from word1 and last
        # from word2.
        # for i in range(n-1, -1, -1):
        #    for j in range(i+1, n):
        #         if(word[i] == word[j]):
        #             dp[i][j] = 2 + dp[i+1][j-1]
        #             if i< n1 and j > n2:
        #                 result = max(result, dp[i][j])
        #         else:
        #         dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        pass
