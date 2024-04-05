from queue import PriorityQueue


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        return self.smallest_range(nums)

    def smallest_range(self, nums: list[list[int]]) -> list[int]:
        # Observation: Use a PriorityQueue to maintain a window of m numbers
        # that include at least one from each row.
        NUM_MAX = 1000000  # Per problem constraints stated
        m = len(nums)
        n = [len(l) for l in nums]
        pq = PriorityQueue()

        max_in_pq, range_left, range_right, min_range = -NUM_MAX, 0, 0, 2 * NUM_MAX

        for i in range(m):
            pq.put((nums[i][0], (i, 0)))
            max_in_pq = max(max_in_pq, nums[i][0])

        while True:
            min_in_pq, (row, col) = pq.get()
            curr_range = max_in_pq - min_in_pq
            if curr_range < min_range:
                min_range = curr_range
                range_left, range_right = min_in_pq, max_in_pq
            if col == n[row] - 1:
                break
            pq.put((nums[row][col + 1], (row, col + 1)))
            max_in_pq = max(nums[row][col + 1], max_in_pq)

        return [range_left, range_right]
