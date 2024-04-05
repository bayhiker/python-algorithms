from queue import PriorityQueue


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        return self.total_cost(costs, k, candidates)

    def total_cost(self, costs: list[int], k: int, candidates: int) -> int:
        pq = PriorityQueue()
        n = len(costs)

        def is_left(i: int) -> bool:
            return i <= n // 2

        l, r = 0, n - 1
        while l < r and l < candidates and r > n - candidates:
            pq.put((costs[l], l))
            pq.put((costs[r], r))
            l += 1
            r -= 1
        count = 0
        total_cost = 0
        while count < k:
            (c, i) = pq.get()
            total_cost += c
            if is_left(i):
                if is_left(l):
                    pq.put(costs[l], l)
                    l += 1
            else:
                if not is_left(r):
                    pq.put(costs[r], r)
                    r -= 1
        return total_cost
