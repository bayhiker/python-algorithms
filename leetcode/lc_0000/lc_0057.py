class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        # Use bisect_right(start) to find i1, and bisect_right(end) to find i2
        # Intervals i1...i2 should be merged together (optionally i1-1 if end_(i1-1) < start
        # Note that you don't have to go through all i1...i2 to do this because the
        # intervals in between i1 and i2 (if any) are fully covered by new_interval,
        # you just have to analyze intervals at the two ends
        pass
