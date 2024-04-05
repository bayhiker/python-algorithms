class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        return self.num_times_all_blue(flips)

    def num_times_all_blue(self, flips: list[int]) -> int:
        next_aligned = 0
        n = len(flips)
        total = 0
        for i in range(n):
            # Earliest possible alignment is at location flips[i]
            # For example [3,2,4,1,5], when you see 3, the earliest possible
            # location you would get a prefix aligned is 111xx,
            # because you filled location 3, you need at least two to fill location 1 and 2.
            next_aligned = max(next_aligned, flips[i])
            if next_aligned == i + 1:
                total += 1
        return total
