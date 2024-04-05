from math import gcd
from collections import Counter


class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        return self.largest_component_size_union_find(nums)

    # Union find, TLE
    def largest_component_size_union_find(self, nums: list[int]) -> int:
        # Union find
        n = len(nums)
        visited = list(range(n))
        for i in range(n):
            for j in range(i):
                if visited[i] == visited[j]:
                    continue
                if gcd(nums[i], nums[j]) == 1:
                    continue
                for k in range(n):
                    if visited[k] == visited[i]:
                        visited[k] = visited[j]
        return max(Counter(visited).values())
