class Solution:
    def minPartitions(self, n: str) -> int:
        return self.min_partitions(n)

    def min_partitions(self, n: str) -> int:
        # Observation: Result is max digit value in n
        return int(max(str(n)))
