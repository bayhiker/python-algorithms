from functools import lru_cache
from itertools import combinations
class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        return self.minimum_difference_enum(nums)

    def minimum_difference_enum(self, nums: list[int]) -> int:
        # Since n is no more than 15, we can try to semi-brute-force
        # 1. First separate nums into two halves
        # 2. Get x items from left half and n-x items from right half
        # 3. Sort all possible partial sums from left, sort all n-x combo sums from the right
        # 4. Use two sorted array, tow pointer, binary search to find min distance for (x, n-x) pair
        n = len(nums) // 2
        half_sum = sum(nums) / 2
        min_diff = float('inf')
        for x in range(n):
            sums_left_x = []
            for x_tuple in combinations(nums[:n], x):
                sums_left_x.append(sum(x_tuple))
            sums_left_x.sort()
            y = n - x
            sums_left_y = []
            for y_tuple in combinations(nums[n:], y):
                sums_left_y.append(sum(y_tuple))
            sums_left_y.sort()
            p, q = 0, len(sums_left_y)-1
            while p < len(sums_left_x) and q >= 0:
                curr_sum = sums_left_x[p] + sums_left_y[q]
                min_diff = min(min_diff, 2*abs(half_sum - curr_sum))
                if curr_sum > half_sum:
                    q -= 1
                elif curr_sum < half_sum:
                    p += 1
                else: # Found a perfect half sum, distance is 0
                    return 0 
        return int(min_diff)


    def minimum_difference_knapsack(self, nums: list[int]) -> int:
        # Knapsack problem: pick n items to get as close to sum(nums)/2 as possible
        nums.sort()
        n = len(nums) // 2
        sums = [nums[0]]
        for i in range(1, n*2):
            sums.append(nums[i] + sums[i-1])
        target_sum = sums[2*n - 1] / 2
        curr_min_diff = float('inf')

        @lru_cache # TLE
        def knapsack(s, m, k):
            # Get min(abs(s, sum of k items in nums[:m+1]))
            if k > m+1:
                return float('inf')
            if k == m+1:
                return s - sums[m] 
            if k == 1:
                return s-nums[0]
            min_with_mth = knapsack(s - nums[m], m-1, k-1)
            min_without_mth = knapsack(s, m-1, k)
            return min_with_mth if abs(min_with_mth)<abs(knapsack(s, m-1, k)) else min_without_mth
        
        return int(2 * abs(knapsack(sums[2*n-1]/2, n*2-1, n)))