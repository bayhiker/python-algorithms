class Solution:
    def minOperations(self, logs: list[str]) -> int:
        return self.min_operations(logs)

    def min_operations(self, logs: list[str]) -> int:
        level = 0
        for log in logs:
            if log == "./":
                pass
            elif log == "../":
                level = max(0, level - 1)
            else:
                level += 1
        return level
