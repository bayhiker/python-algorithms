"""
You have n buckets each containing some gallons of water in it,
represented by a 0-indexed integer array buckets, where the ith
bucket contains buckets[i] gallons of water. You are also given an integer loss.

You want to make the amount of water in each bucket equal.
You can pour any amount of water from one bucket to another bucket
(not necessarily an integer). However, every time you pour k gallons of water,
you spill loss percent of k.

Return the maximum amount of water in each bucket after making the amount
of water equal. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: buckets = [1,2,7], loss = 80
Output: 2.00000
Explanation: Pour 5 gallons of water from buckets[2] to buckets[0].
5 * 80% = 4 gallons are spilled and buckets[0] only receives 5 - 4 = 1 gallon of water.
All buckets have 2 gallons of water in them so return 2.

Example 2:

Input: buckets = [2,4,6], loss = 50
Output: 3.50000
Explanation: Pour 0.5 gallons of water from buckets[1] to buckets[0].
0.5 * 50% = 0.25 gallons are spilled and buckets[0] only receives 0.5 - 0.25 = 0.25 gallons of water.
Now, buckets = [2.25, 3.5, 6].
Pour 2.5 gallons of water from buckets[2] to buckets[0].
2.5 * 50% = 1.25 gallons are spilled and buckets[0] only receives 2.5 - 1.25 = 1.25 gallons of water.
All buckets have 3.5 gallons of water in them so return 3.5.

Example 3:

Input: buckets = [3,3,3,3], loss = 40
Output: 3.00000
Explanation: All buckets already have the same amount of water in them.

 

Constraints:

    1 <= buckets.length <= 105
    0 <= buckets[i] <= 105
    0 <= loss <= 99

"""


class Solution:
    def equalizeWater(self, buckets: list[int], loss: int) -> float:
        return self.equalize_water(buckets, loss)

    def equalize_water(self, buckets: list[int], loss: int) -> float:
        #
        # Observation:
        # Use amount of water wasted to find an equation,
        #   let x be the final water amount, n = len(buckets)
        #   sum(buckets) - n*x = k(sum(abs(buckets[i] - x)))
        # In order to remove the abs() layer to get x,
        # we do a binary search of which [buckets[i], buckets[i+1]]
        # interval x falls into
        n = len(buckets)
        total = sum(buckets)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            min_x, max_x = buckets[mid], buckets[mid + 1]
            equal_amount = (total - loss / 100.0 * sum(buckets[mid + 1 :])) / (
                n - loss / 100.0 * (n - 1 - mid)
            )
            # Set precision to 5 digits after decimal point
            equal_amount = round(equal_amount, 5)
            if equal_amount > max_x:
                left = mid + 1
                continue
            elif equal_amount < min_x:
                right = mid
                continue
            else:
                return equal_amount
