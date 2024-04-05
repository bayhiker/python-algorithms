class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        # DP: dp_start[i], and dp_end[i]: Arrays representing all possible
        #     disjoint square streaks in nums[0..i],
        #     where disjoint means streaks that cannot be merged. E.g., 1,4,9 and 9,16 are
        #     not disjoint, they should be merged into 1,4,9,16.
        #     Each item in the array is <start, length>
        #
        #     dp[i+1] =
        #          dp[i] if nums[i+1] is not perfect square, otherwise,
        #          look up sqrt[nums[i+1]] in dp_start, and merge streaks.
        #          Note that streaks in dp[i] are disjoint, therefore
        #                dp_start[k] - dp_end[k-1] > 1 (otherwise they should have been merged)
        #     This is O(n*log(m)), where m is the number of perfect squares. Worst case O(n*log(n))
        #
        # Non-DP: first filter thru the list nums for perfect squares into ps[] of size m
        #      sort ps, go through them one by one to look for longest streaks.
        #     This is O(n + m*log(m), worst case O(n*log(n))
        pass
