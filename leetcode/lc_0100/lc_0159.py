"""

159. Longest Substring with At Most Two Distinct Characters

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        return self.length_of_longest_substring_two_distinct(s)

    def length_of_longest_substring_two_distinct(self, s: str) -> int:
        # Use two-pointers, use a hash to record freq of chars in curr window
        pass
