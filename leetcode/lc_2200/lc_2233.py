from math import ceil, floor
from functools import reduce


class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        return self.maximum_product(nums, k)

    def maximum_product(self, nums: list[int], k: int) -> int:
        # Observation: max product is achieved by increasing the smaller nums as much as possible
        # Imagine there is a sea level line that rises from min(nums),
        # use k to fill them smaller nums as the sea level rises
        nums.sort()
        sum, n = 0, len(nums)
        for i, num in enumerate(nums):
            sum += num
            if i == n - 1 or sum + k <= nums[i + 1] * (i + 1):
                break
        avg = (sum + k) / (i + 1)
        c, f = ceil(avg), floor(avg)
        f_count = c * (i + 1) - (sum + k)
        c_count = i + 1 - f_count
        return (
            c**c_count
            * f**f_count
            * reduce(lambda x, y: x * y, nums[i + 1 :], 1)
            % (10**9 + 7)
        )
