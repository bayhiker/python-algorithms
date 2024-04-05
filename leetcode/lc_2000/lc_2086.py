"""given a street represented by a string where 'H' denotes
a house, 'B' a bucket, and '.' an empty space. Our task is
to find the minimum number of buckets we need to place on
the street such that every house has a bucket to its left
or its right. If this is not possible, return -1.
"""


class Solution:
    def minimumBuckets(self, street: str) -> int:
        return self.minimum_buckets(street)

    def minimum_buckets(self, street: str) -> int:
        # Use greedy algorithm. For each house:
        # 1. If the house already has a bucket on its left or right,
        # move on to the next house
        # 2. If the house doesn't have a bucket on its left or right,
        # Put a bucket on its right if there's an empty lot, otherwise
        # if there is an empty lot on the left side, put a bucket on
        # its left, buckets += 1. If there's not an empty lot on its
        # left side, return -1
        pass
