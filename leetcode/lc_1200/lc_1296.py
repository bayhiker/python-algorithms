class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        return self.is_possible_divide(nums, k)
        
    def is_possible_divide(self, nums: list[int], k: int) -> bool:
        from typing import Counter
        counter = Counter(nums)
        nums.sort()
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if counter[num] > 0:
                for x in range(num, num+k):
                    if x in counter and counter[x] > 0:
                        counter[x] -= 1
                    else:
                        return False
        return True