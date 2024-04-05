from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        return self.min_deletions(s)

    def min_deletions(self, s: str) -> int:
        # Sort occurrences in non-increasing order
        counts = sorted(list(Counter(s).values()), key=lambda x: -x)
        # Starting from max count, find the next available non-dup spot it could take
        removed, available = 0, counts[0]
        for count in counts:
            # If my spot taken, occupy next available by removing chars,
            # If next available doesn't exist, remove all my chars
            if available < 0:
                removed += count
                continue
            if count > available:
                removed += count - available
            else:
                available = count
            available -= 1  # I can take my current space
        return removed
