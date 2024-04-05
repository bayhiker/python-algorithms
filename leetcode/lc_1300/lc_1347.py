from typing import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return self.min_steps(s, t)

    def min_steps(self, s: str, t: str) -> int:
        counter_s, counter_t = Counter(s), Counter(t)
        total = 0
        for i in counter_s:
            total += abs(counter_s[i] - (counter_t[i] if i in counter_t else 0))
        for j in counter_t:
            total += 0 if j in counter_s else counter_t[j]
        return total // 2
