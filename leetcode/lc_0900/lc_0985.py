class Solution:
    def sumEvenAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        return self.sum_even_after_queries(nums, queries)

    def sum_even_after_queries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        # Use s to store current sum of even values
        # For each query (v, i):
        #   if nums[i] is even and v is even, s += v
        #                 even and v is odd, s -= nums[i]
        #                 odd and v is even, s doesn't change
        #                 odd and v is odd, s += v + nums[i]
        #   nums[i] += v
        pass
