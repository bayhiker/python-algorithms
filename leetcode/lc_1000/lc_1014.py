class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        return self.max_score_sightseeing_pair(values)

    def max_score_sightseeing_pair(self, values: list[int]) -> int:
        # Pair score = values[i] + i + value[j] - j for any i < j
        # If a fixed j is in the result pair, then it must pair with
        # max (values[i] + i) for any i in 0..j-1
        # Therefore we can do this in one values traversal if we
        # memoize the current max(value[i] + i)
        max_i_sum = 0  # i_sum is values[i] + i
        n = len(values)
        max_pair = 0
        for i in range(n - 1):
            curr_i_sum = values[i] + i
            if curr_i_sum > max_i_sum:
                max_i_sum = curr_i_sum
            curr_j_sum = values[i + 1] - i - 1
            if max_i_sum + curr_j_sum > max_pair:
                max_pair = max_i_sum + curr_j_sum
        return max_pair
