from queue import PriorityQueue


class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        return self.k_sum(nums, k)

    def k_sum(self, nums: list[int], k: int) -> int:
        # Get largest sum: sum of all non-negative nums,
        n = len(nums)
        max_sum = 0
        for i in range(n):
            if nums[i] > 0:
                max_sum += nums[i]
            elif nums[i] < 0:
                nums[i] = -nums[i]

        nums.sort()
        pq = PriorityQueue()
        # (sum of nums to remove from max_sum, largest num index in nums to remove)
        pq.put((nums[0], 0))
        # Get (k-1)th smallest from pq, counting in max_sum, we have k'th
        items_sum = 0
        for _ in range(0, k - 1):
            (items_sum, i) = pq.get()
            if i < n - 1:
                pq.put((items_sum + nums[i + 1], i + 1))
                pq.put((items_sum - nums[i] + nums[i + 1], i + 1))
        return max_sum - items_sum
