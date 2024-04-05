class Solution:
    def mincostToHireWorkers(
        self, quality: list[int], wage: list[int], k: int
    ) -> float:
        return self.min_cost_to_hire_workers(quality, wage, k)

    def min_cost_to_hire_workers(
        self, quality: list[int], wage: list[int], k: int
    ) -> float:
        # Use greedy algorithm
        # Sort workers by wage/quality in increasing order
        # Put worker in max heap one by one, ordered by quality, until heap reaches size k
        # Record total wage
        # Keep adding workers one by one into the max heap, pop out root to keep heap size k
        # Update total wage if current total in heap is smaller
        pass
