class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        return self.sum_subarray_mins_monotonic_stack(arr)

    def sum_subarray_mins_monotonic_stack(self, arr: list[int]) -> int:
        """
        Observation: for arr [2,7,6,5,4,5,6,1], there are 4*3 contiguous sub-arrays
                     with 4 as their smallest. The subarray could go as far left as
                     7, and go as far right as 6.
        So this problem becomes a problem of looking for left_smaller and right_smaller
        of each element in arr. This can be achieved with a monotonic stack as below.
        Todo: right_smaller can be eliminated. Every time we pop from stock, we calculate
        and update sum.
        """
        n = len(arr)
        s: list[int] = []
        left_smaller: list[int] = [-1] * n
        right_smaller: list[int] = [n] * n
        for i in range(n):
            while s and arr[i] < arr[s[-1]]:
                right_smaller[s[-1]] = i
                s.pop()
            if s:
                left_smaller[i] = s[-1]
            s.append(i)
        sum = 0
        modulo = 10**9 + 7
        for i in range(n):
            sum = (
                sum + arr[i] * (i - left_smaller[i]) * (right_smaller[i] - i)
            ) % modulo
        return sum

    def sum_subarray_mins_contiguous_subarray_dp(self, arr: list[int]) -> int:
        n = len(arr)
        min_sum = 0
        minimums: list[int] = [3 * 10**4 for j in range(n)]
        modulo = 10**9 + 7
        for i in range(n):
            for j in range(i + 1):
                minimums[j] = min(minimums[j], arr[i])
                min_sum = (min_sum + minimums[j]) % modulo
        return min_sum

    def sum_subsequence_mins_any_subarray(self, arr: list[int]) -> int:
        """
        If we modify the problem by allowing any sub-sequence, not necessarily contiguous.
        Then for size k sub-sequence:
          (n-1)C(k-1) has sorted_arr[0]
          (n-2)C(k-1) has sorted_arr[1] but not [0]
          (n-3)C(k-1) has sorted_arr[2] but not 0, 1
          ...
          (k-1)C(k-1) has sorted_arr[n-k] but not 0, 1, ..., n-k-1
        """
        arr.sort()
        pow_of_two = 1
        n = len(arr)
        modulo = 10**9 + 7
        sum = arr[n - 1]
        for i in range(1, n):
            pow_of_two *= 2
            sum = (sum + pow_of_two * arr[n - 1 - i]) % modulo
        return sum
