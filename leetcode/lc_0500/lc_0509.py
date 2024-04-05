class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev = 0
        curr = 1
        for i in range(2, n + 1):
            next = prev + curr
            prev = curr
            curr = next
        return curr
