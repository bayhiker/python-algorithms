class Solution:
    def numMovesStonesII(self, stones: list[int]) -> list[int]:
        return self.num_moves_stones_ii(stones)

    def num_moves_stones_ii(self, stones: list[int]) -> list[int]:
        # stones.sort()
        # To get max, use 2-pointer.
        # Observations:
        # 1. The ideal max is the sum of all spaces between stones[0] and stones[n-1]
        # 2: If there's space next to end stone, when you move it, those spaces disappear
        # (or are wasted)
        # Use two pointers pointing to two ends. Move them towards each other if possible,
        # minimize wasted spaces along the way.
        #
        # To get min, use a sliding window of size n, count and get the max number of
        # rocks in the window max_rocks. Min is n - max_rocks. If max_rocks is n-1 though,
        # meaning all but 1 rock are already connected. Instead of 1, we need two steps.
        # e.g., 3,4,5,6,10. 10 cannot be moved next 6. First move 3 to 8, and move 10 to 7.
        pass
