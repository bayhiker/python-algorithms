class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        return self.chalk_replacer(chalk, k)

    def chalk_replacer(self, chalk: list[int], k: int) -> int:
        s = sum(chalk)
        k = k % s
        total = 0
        for i in range(len(chalk)):
            total += chalk[i]
            if total > k:
                break
            i += 1
        return i
