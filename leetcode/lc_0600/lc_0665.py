class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        return self.check_possibility(nums)

    def check_possibility(self, nums: list[int]) -> bool:
        # Use a monotonic stack to keep items in order
        modified = False
        for i in range(1, len(nums)):
            num = nums[i]
            if num >= nums[i - 1]:
                continue
            # now we know num < nums[i-1]
            if modified:  # 1 modification quota already used, cannot modify any more
                return False
            modified = True
            if i == 1 or num >= nums[i - 2]:
                # If possible, we prefer making last element smaller
                nums[i - 1] == num
            else:  # Not an option to decrease last element, then increase num
                nums[i] = nums[i - 1]
        return True
