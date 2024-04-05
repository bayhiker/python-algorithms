class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        return self.find_different_binary_string(nums)

    def find_different_binary_string(self, nums: list[str]) -> str:
        n = len(nums)  # By constraints len(nums[0]) is also n
        d = {int(num, 2): True for num in nums}
        for i in range(n + 1):
            if not i in d:
                return format(i, f"0{n}b")
        return None
