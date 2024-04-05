from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        return self.find_shortest_sub_array(nums)

    def find_shortest_sub_array(self, nums: list[int]) -> int:
        # key is num, value is [count, start_index, end_index]
        d: dict[int:[int, int, int]] = {}
        max_freq = 0
        max_nums = []
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = [1, i, i]
            else:
                d[num][0] += 1
                d[num][2] = i
            freq = d[num][0]
            if freq > max_freq:
                max_freq = freq
                max_nums = [num]
            elif freq == max_freq:
                max_nums.append(num)
        degree = len(nums)
        for num in max_nums:
            num_info = d[num]
            degree = min(degree, num_info[2] - num_info[1] + 1)
        return degree
