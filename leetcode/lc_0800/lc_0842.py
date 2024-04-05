class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        return self.split_into_fibonacci(num)

    def split_into_fibonacci(self, num: str) -> list[int]:
        # Use a stack to store the fib-compliant number so far
        n = len(num)
        result: list[int] = []
        for i in range(n // 2):  # first number cannot be more than half of num
            if num[0] == "0" and i >= 1:  # No number start with 0 except 0 itself
                break
            first = int(num[0 : i + 1])
            if first >= 2**31:
                break
            for j in range(i + 1, n - i):
                if num[i + 1] == "0" and j >= i + 2:
                    break
                if i > n - j or j - i > n - j:
                    # Not enough digits for a valid third number
                    break
                result = []
                # leave at least max(first, second) digits for third num
                result.append(first)
                second = int(num[i + 1 : j + 1])
                if second >= 2**31:
                    break
                result.append(second)
                k = j
                while True:
                    next_num = result[-1] + result[-2]
                    next_str = str(next_num)
                    if next_num >= 2**31:
                        break
                    if num[k + 1 :].startswith(next_str):
                        result.append(next_num)
                        k += len(next_str)
                    else:
                        break
                    if k == n - 1:
                        return result
        return []
