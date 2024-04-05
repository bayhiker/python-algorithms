class Solution(object):
    def twoSum(self, nums, target):
        return self.two_sum(nums, target)

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index: dict[int, int] = {}
        for i in range(0, len(nums)):
            # Build the hash as we go
            num = nums[i]
            complement = target - nums[i]
            if complement in num_index:
                return [num_index[complement], i]
            num_index[num] = i
        return None
