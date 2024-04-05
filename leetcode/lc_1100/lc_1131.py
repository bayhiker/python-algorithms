class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        return self.max_abs_val_expr(arr1, arr2)

    def max_abs_val_expr(self, arr1: list[int], arr2: list[int]) -> int:
        # Solution 1: dp
        # f(i, j) = |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
        # dp[m]: max(f(i, j)) from arr1[0:m] arr2[0:m]
        # dp[m+1]: max(dp[m], f(0, m+1), f(1, m+1), ....)
        # O(n**2)
        pass

        # Solution 2: math
        """
        |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j| =
        if i>=j
        (arr1[i] + arr2[i] + i) - (arr1[j] + arr2[j] + j) if arr1[i] >= arr1[j], arr2[i] >= arr2[j]
        (arr1[i] - arr2[i] + i) - (arr1[j] - arr2[j] + j) if arr1[i] >= arr1[j], arr2[i] < arr2[j]
        (-arr1[i] - arr2[i] + i) - (-arr1[j] + arr2[j] + j) if arr1[i] < arr1[j], arr2[i] >= arr2[j]
        (-arr1[i] + arr2[i] + i) - (-arr1[j] - arr2[j] + j) if arr1[i] < arr1[j], arr2[i] < arr2[j]
        if i<j
        (arr1[i] + arr2[i] - i) - (arr1[j] + arr2[j] - j) if arr1[i] >= arr1[j], arr2[i] >= arr2[j]
        (arr1[i] - arr2[i] - i) - (arr1[j] - arr2[j] - j) if arr1[i] >= arr1[j], arr2[i] < arr2[j]
        (-arr1[i] - arr2[i] - i) - (-arr1[j] + arr2[j] - j) if arr1[i] < arr1[j], arr2[i] >= arr2[j]
        (-arr1[i] + arr2[i] - i) - (-arr1[j] - arr2[j] - j) if arr1[i] < arr1[j], arr2[i] < arr2[j]

        Because arr1 and arr2 are symmetric in this case, we need to look at the following 4 cases:
        l1 = arr1[i] + arr2[i] + i
        l2 = arr1[i] + arr2[i] - i
        l3 = arr1[i] - arr2[i] + i
        l4 = arr1[i] - arr2[i] - i

        max (f(i, j)) = max (
            max(l1) - min(l1))
            max(l2) - min(l2))
            max(l3) - min(l3))
            max(l4) - min(l4))

        O(n)
        """
