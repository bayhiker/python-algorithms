from queue import PriorityQueue
from functools import total_ordering
from lib.number import factorize


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        return self.maximum_score(nums, k)

    def maximum_score(self, nums: list[int], k: int) -> int:
        total = len(nums)
        pq = PriorityQueue()
        prime_scores: list[int] = []
        left: list[int] = [
            0
        ] * total  # Number of continuously strictly increasing numbers on the left
        right: list[int] = [
            0
        ] * total  # Number of continuously non-increasing numbers on the right
        # Init prime_score list, and priority queue sorted by nums[i]
        for i in range(0, len(nums)):
            pq.put(Num(nums[i], i))
            prime_scores.append(len(factorize(nums[i])))
        # Init left and right of nums in priority queue based on prime scores
        for i in range(0, total):
            if i < total - 1 and prime_scores[i] < prime_scores[i + 1]:
                left[i + 1] = left[i] + 1
            if i > 0 and prime_scores[total - 1 - i] >= prime_scores[total - i]:
                right[total - i - 1] = right[total - i] + 1
        debug_num_pq(pq, nums, prime_scores, left, right)
        # Calculate max score
        max_score = 1
        while k >= 0 and not pq.empty():
            max_num: Num = pq.get()
            i = max_num.index
            possible_ranges = (left[i] + 1) * (right[i] + 1)
            repeat = possible_ranges if k > possible_ranges else k
            print(
                f"max_num is {max_num.n}, index is {i}, score is {prime_scores[i]}, ranges: {possible_ranges}"
            )
            max_score *= max_num.n**repeat
            max_score %= 10**9 + 7
            k -= repeat
        return max_score


@total_ordering
class Num(object):
    index: int = -1

    def __init__(self, n: int, index: int) -> None:
        self.n = n  # Number
        self.index = index  # Index of n in nums array

    def __lt__(self, other):
        return self.n > other.n

    def __eq__(self, other) -> bool:
        return self.n == other.n


def debug_num_pq(
    pq: PriorityQueue,
    nums: list[int],
    prime_scores: list[int],
    left: list[int],
    right: list[int],
) -> None:
    # NOTE: this section drains the pq and changes program logic
    # while not pq.empty():
    #   num: Num = pq.get()
    #   i = num.index
    #   print(f"num is n:{num.n}, index: {num.index}, score: {prime_scores[i]}, left: {left[i]}, right: {right[i]}")
    for i in range(len(nums)):
        print(
            f"num is :{nums[i]}, index: {i} score: {prime_scores[i]}, left: {left[i]}, right: {right[i]}"
        )
