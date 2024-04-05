class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        return self.minimum_swap(s1, s2)

    def minimum_swap(self, s1: str, s2: str) -> int:
        x2y, y2x = 0, 0
        for i in range(len(s1)):
            if s1[i] == "x" and s2[i] == "y":
                x2y += 1
            elif s1[i] == "y" and s2[i] == "x":
                y2x += 1
        if (x2y % 2 == 1 and y2x % 2 == 0) or (x2y % 2 == 0 and y2x % 2 == 1):
            return -1
        # There's and xy-> yx or yx->xy, you need 2 swaps xy/yx -> xx/yy->xy/xy
        min_swaps = 2 if x2y % 2 and y2x % 2 else 0
        min_swaps += x2y // 2 + y2x // 2
        return min_swaps
