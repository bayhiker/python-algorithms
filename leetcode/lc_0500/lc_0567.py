from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.check_inclusion(s1, s2)

    def check_inclusion(self, s1: str, s2: str) -> bool:
        # two-pointer to track a window of len(s1) in s2
        # Use dict to track freq of letters in s1 and in current window of s2
        m = len(s1)
        counter_s1 = Counter(s1)
        p, q = 0, m - 1
        counter_s2_window = Counter(s2[0:m])
        while q < len(s2):
            match = True
            for c in counter_s1.keys():
                if c not in counter_s2_window or counter_s2_window[c] != counter_s1[c]:
                    match = False
                    break
            if match:
                return True
            p, q = p + 1, q + 1
            if q >= len(s2):
                break
            char_out, char_in = s2[p - 1], s2[q]
            if counter_s2_window[char_out] == 1:
                counter_s2_window.pop(char_out)
            else:
                counter_s2_window[char_out] -= 1
            if char_in in counter_s2_window:
                counter_s2_window[char_in] += 1
            else:
                counter_s2_window[char_in] = 1
        return False
