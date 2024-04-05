class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Solution 1:
        Use left_peak[i] and right_peak[i] for each height[i],
        amount of water trapped on height[i] is min(right_peak[i], left_peak[i]) - height[i] if > 0

        To init left_peak[i], start from height[0], use left_max to track current max seen,
        and assign left_peak[i] = left_max. Similarly init right_peak[i]

        Time and space O(n)

        Solution 2:
        Use left_max and right_max to track max height seen so far from left and right.
        Use two pointers i=0 and j=n-1, and move them until they meet.
        if left_max < right_max, then look at the height[i] and check how much water it can hold
        note that the maximum peak to the right of height[i] may be larger than current right_max,
        however, that doesn't matter because the amount of water trapped at i is limited by left_max
        if left_max >= right_max, then process j similarly.
        repeat until i and j meet



        Args:
            height (list[int]): _description_

        Returns:
            int: _description_
        """
        pass
