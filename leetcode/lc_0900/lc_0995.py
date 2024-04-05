from collections import deque


class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        return self.min_k_bit_flips_reuse_nums(nums, k)

    def min_k_bit_flips_queue(self, nums: list[int], k: int) -> int:
        # Greedy, start from the first 0, track whether how many times a bit has been flipped
        # Option 1: use a queue to track last index of each k-bit flip.
        # If current index smaller than head of queue, then current item has been flipped len(queue) times
        # If current index equals queue head, then dequeue it
        dq = deque()
        count = 0
        n = len(nums)
        for i in range(n):
            if len(dq) % 2 == nums[i]:
                if n - i < k:
                    return -1
                count += 1
                dq.append(i + k - 1)
            if dq and i == dq[0]:
                dq.popleft()
        return count

    def min_k_bit_flips_reuse_nums(self, nums: list[int], k: int) -> int:
        # Greedy, start from the first 0, track whether how many times a bit has been flipped
        # Option 2: Use one single int flips: number of flips for nums[i]
        #           Use nums[j] to flag if nums[j] is the last affected number of a previous flip,
        #                 by adding 2 to its current value
        #     when we do a flip, flips += 1. Once a nums[x] >= 2 is processed, meaning
        #     all numbers affected by the flip that ended at nums[x] has been processed, then flips -= 1
        flips, count = 0, 0
        n = len(nums)
        for i in range(n):
            if flips % 2 == nums[i] % 2:
                if n - i < k:
                    return -1
                count += 1
                flips += 1
                nums[i + k - 1] += 2
            if nums[i] >= 2:
                nums[i] -= 2
                flips -= 1
        return count
