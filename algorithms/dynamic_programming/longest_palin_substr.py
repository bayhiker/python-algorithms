# leetcode_5
# Given a string, return the longest palindromic substring


def is_palindrome(s):
    if s is None or len(s) == 0:
        return False
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return i >= j


# Bruteforce: find all substrings and check if it is a palindrome
def get_longest_brute_force(s):
    if not s or len(s) == 0:
        return None
    palin_start = 0
    palin_length = 0
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i : j + 1]):
                if j + 1 - i > palin_length:
                    palin_start = i
                    palin_length = j + 1 - i
    return s[palin_start : palin_start + palin_length]


# Key to DP solution is the state transition: dp[i][j] = s[i] == s[j] and dp[i-1][j-1]
def get_longest_dp(s):
    if not s or len(s) == 0:
        return None
    dp = [[False for i in range(0, len(s))] for j in range(0, len(s))]
    for i in range(0, len(s)):
        dp[i][i] = True
    longest_start = 0
    longest_end = 0
    for i in range(len(s) - 1, -1, -1):
        # i loops from len(s) to 0 because we need dp[i+1][j-1] to get dp[i][j]
        for j in range(i, len(s)):
            if j == i:
                dp[i][j] = True
            elif j == i + 1:
                dp[i][j] = s[i] == s[i + 1]
            else:
                # Now we are sure j-i > 1
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
            if dp[i][j] and j - i >= longest_end - longest_start:
                # If we want to find the last longest, then use j-i > longest_end - longest_start
                longest_start = i
                longest_end = j
    return s[longest_start : longest_end + 1]
