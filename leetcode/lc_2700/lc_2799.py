class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        return self.count_complete_subarrays(nums)

    def count_complete_subarrays(self, nums: list[int]) -> int:
        # Use two pointers l and r, total = len(set(nums))
        # 1. Both l and r start from 0
        # 2. move r to the right until a subarray has all letters.
        #    To verify, use a Hash h to store occurrences of letters.
        # 3. First move l forward until size of h is less than total,
        #    then start moving r until len(h) == total.
        # 4. Keep repeating until r reaches end of nums, and l cannot
        #    move right any more.
        pass
