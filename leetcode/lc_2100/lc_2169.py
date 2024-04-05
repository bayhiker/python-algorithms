class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        return self.count_operations_iteration(num1, num2)

    # Iteration is way faster than recursion
    def count_operations_iteration(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
        return count

    def count_operations_recursive(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        if num1 == num2:
            return 1
        return (
            1 + self.count_operations(num1 - num2, num2)
            if num1 > num2
            else 1 + self.count_operations(num1, num2 - num1)
        )
