class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        return self.sum_of_three(num)

    def sum_of_three(self, num: int) -> list[int]:
        if num % 3:
            return []
        one_third = int(num / 3)
        return [one_third - 1, one_third, one_third + 1]
