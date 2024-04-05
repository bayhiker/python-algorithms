class FrequencyTracker:
    def __init__(self):
        self.nums: {int: int} = {}
        self.freq: {int: list[int]} = {}

    def add(self, number: int) -> None:
        # If number in nums, increase self.nums[number] by 1, then move number in self.freq accordingly
        # if number not in nums, add number to nums and freq
        # Worst case O(1)
        pass

    def deleteOne(self, number: int) -> None:
        # if self.nums[number] exists and > 1, decrease self.nums[number] and move number in self.freq
        # if self.nums[number] is 1, remove number from both self.nums and self.freq
        # Usually close to O(1), worst case O(n)
        pass

    def hasFrequency(self, frequency: int) -> bool:
        # O(1), depending on hashing quality
        return frequency in self.freq


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
