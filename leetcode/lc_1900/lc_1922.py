class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return self.count_good_numbers(n)

    def count_good_numbers(self, n: int) -> int:
        dp: list[int] = []  # dp[i] total for 2*i digits
        modulo = 10**9 + 7
        i = 0
        while 2**i <= n:
            if i == 0:
                dp.append(5)
            elif i == 1:
                dp.append(20)
            else:
                dp.append((dp[i - 1] * dp[i - 1]) % modulo)
            i += 1

        total = 1
        for i in range(len(dp) - 1, -1, -1):
            if n >= 2**i:
                n -= 2**i
                total = (total * dp[i]) % modulo
        return total
