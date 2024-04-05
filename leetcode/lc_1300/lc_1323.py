class Solution:
    def maximum69Number(self, num: int) -> int:
        return self.maximum_69_number(num)

    def maximum_69_number(self, num: int) -> int:
        # Find the first 6 from the left, change it to 9
        # If no 6 found, return original number
        return int(str(num).replace("6", "9", 1))
