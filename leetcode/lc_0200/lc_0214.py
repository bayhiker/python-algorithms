class Solution:
    def shortestPalindrome(self, s: str) -> str:
        return self.shortest_palindrome_kmp(s)

    def shortest_palindrome_kmp(self, s: str) -> str:
        # Use partial match table (next table) in kmp algorithm
        # Observation: Use next table of s to match string s_reverse,
        # When i and j meet at index k, that's our longest palindrome s[0:2k]

        # Get next table 
        n, next =len(s), [0]
        p, i = 0, 1
        while i < n:
            if s[i] == s[p]:
                next.append(next[i-1] + 1)
                i, p = i + 1, p + 1
            else: # p > 0 and s[i] != [p]
                while s[i] != s[p] and p>0:
                    p = next[p-1]
                if s[i] == s[p]:
                    next.append(p + 1)
                    i, p = i+1, p+1
                else:
                    next.append(0)
                    i = i + 1
        # Use next table to match s-reverse
        i, p = n - 1, 0
        while i > 0 and i > p:
            if s[i] == s[p]:
                i, p = i - 1, p + 1
            else:
                while s[i] != s[p] and p > 0:
                    p = next[p-1]
                if p == 0:
                    i -= 1
        return s[-1:i+p:-1] + s
            





        pass

    def shortest_palindrome_naive(self, s: str) -> str:
        # Naive approach, TLE, find longest palindrome s[0:i]
        n = len(s)
        if n == 0:
            return ""
        for i in range(n - 1, -1, -1):
            p, q = 0, i
            found = True
            while q > p:
                if s[p] != s[q]:
                    found = False
                    break
                p += 1
                q -= 1
            if found:
                break
        return s[i + 1 :][::-1] + s
