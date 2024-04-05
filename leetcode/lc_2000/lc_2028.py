class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        return self.missing_rolls_average(rolls, mean, n)

    def missing_rolls_average(self, rolls: list[int], mean: int, n: int) -> list[int]:
        n_sum = mean * (n + len(rolls)) - sum(rolls)
        if n_sum > 6 * n or n_sum < n:
            return []
        average = n_sum // n
        remainder = n_sum - average * n
        return [average] * (n - remainder) + [average + 1] * remainder

    def missing_rolls_dfs(self, rolls: list[int], mean: int, n: int) -> list[int]:
        # Accepted, but slow
        n_sum = mean * (n + len(rolls)) - sum(rolls)

        # Find n numbers between 1-6 adding up to n_sum
        # DFS with trimming
        stack: list[int] = []  # stores current roll assignments

        def dfs(curr_sum: int):
            count = n - len(stack)
            if count * 6 < n_sum - curr_sum or count > n_sum - curr_sum:
                if stack:
                    stack.pop()
                return
            if count == 1:
                stack.append(n_sum - curr_sum)
                return
            for i in range(1, 7):
                stack.append(i)
                dfs(curr_sum + i)
                if len(stack) == n:
                    return

        dfs(0)
        return stack if stack else []
