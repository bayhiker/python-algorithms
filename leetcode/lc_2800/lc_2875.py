from itertools import accumulate


class Solution:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        return self.min_size_subarray_2p(nums, target)

    def min_size_subarray_2p(self, nums: list[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        loops = target // total
        remainder = target % total
        if remainder == 0:
            return n * loops
        nums2 = nums + nums  # Handle circular scenario
        p1, p2 = 0, 0
        total = nums2[0]
        min_length = n + 1
        while p2 < n * 2:
            if total == remainder:
                min_length = min(min_length, p2 - p1 + 1)
                total -= nums2[p1]
                p1 += 1
            elif total < remainder:
                p2 += 1
                if p2 == n * 2:
                    break
                total += nums2[p2]
            else:
                total -= nums2[p1]
                p1 += 1
        return -1 if min_length == n + 1 else loops * n + min_length

    def min_size_subarray_partial_sum(self, nums: list[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        loops = target // total
        remainder = target % total
        if remainder == 0:
            return n * loops
        # Now the problems becomes find subarray of nums adding up to remainder
        sums = [0] + list(accumulate(nums))
        min_length = n + 1  # valid length can never go above n
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if sums[j] - sums[i] == remainder:
                    min_length = min(min_length, j - i)
                if sums[j] - sums[i] == total - remainder:
                    min_length = min(min_length, i + n - j)
        return -1 if min_length == n + 1 else loops * n + min_length
