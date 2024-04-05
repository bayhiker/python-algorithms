class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return self.find_median_sorted_arrays(nums1, nums2)

    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.find_median_sorted_arrays(nums2, nums1)

        n1, n2 = len(nums1), len(nums2)
        k = (n1 + n2 + 1) // 2
        odd_total = (n1 + n2) % 2
        l, r = 0, n1
        while l <= r:
            p1 = (l + r) // 2  # Length of left partition of nums1
            p2 = k - p1  # Length of left partition of nums2 if median found
            left1 = float("-inf") if p1 == 0 else nums1[p1 - 1]
            right1 = float("inf") if p1 == n1 else nums1[p1]
            left2 = float("-inf") if p2 == 0 else nums2[p2 - 1]
            right2 = float("inf") if p2 == n2 else nums2[p2]

            if left1 <= right2 and left2 <= right1:
                # p1 - 1 to the left of left1
                # p2 - 1 (k - p1 - 1) to the left of left2
                # Total of k-2 to the left of left1 and left2
                if odd_total:
                    # If odd, median is the kth item, max of left1 and left2
                    return max(left1, left2)
                else:
                    # If even, median is average of k'th and (k+1)'th
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = p1 - 1
            else:
                l = p1 + 1
