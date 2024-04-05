class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        # First construct a PriorityQueue pq with Counter(arr), this is O(n)
        # if constructed in on batch (O(n*log(n)) if inserted one by one)
        # Then pop root of pq one by one until k is reached.
        # Finally return size of pq
        pass
