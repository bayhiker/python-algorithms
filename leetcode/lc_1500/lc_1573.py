class Solution:
    def numWays(self, s: str) -> int:
        return self.num_ways(s)

    def num_ways(self, s: str) -> int:
        # Observation: First separate 1s into three groups,
        #     number of splits is the product of num of 0s
        #     between the last 1 of the first 3rd and first 1
        #     of the second 3rd, and the count between the last
        #     1 of the second 3rd and the first 1 of the last third
        n = len(s)
        total_ones = s.count("1")
        if total_ones % 3 > 0:
            return 0

        if total_ones == 0:
            # (n-2) + (n-3) + (n-4) + ... + 2 + 1
            return int((n - 1) * (n - 2) / 2) % (10**9 + 7)
        # total_ones is 3, 6, 9, ...
        count_ones = 0
        count_zeroes_left = 0  # 0s between 1/3 1s and 2/3 1s
        count_zeroes_right = 0  # 0s between 2/3 1s and 3/3 1s
        for digit in s:
            if digit == "1":
                count_ones += 1
            if digit == "0":
                if count_ones == total_ones / 3:
                    count_zeroes_left += 1
                elif count_ones == total_ones * 2 / 3:
                    count_zeroes_right += 1
        return int((count_zeroes_left + 1) * (count_zeroes_right + 1)) % (10**9 + 7)
