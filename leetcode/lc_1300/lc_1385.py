class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        self.find_the_distance_value(arr1, arr2, d)

    def find_the_distance_value(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Sort arr1 and arr2
        # For each item arr1[i], use binary search to find it in arr2,
        # if found, then arr1[i] is not in distance. Otherwise, if arr1[i]
        # falls between arr2[j] and arr2[j+1], then use j, j+1 to check
        # if arr1[i] should increase distance by 1
        # O(m*log(m) + n*log(n) + m*log(n)
        pass
