# Leftmost column with at least a 1
"""
Sorted binary matrix M(rows, cols) where M(i, j) = 0 or 1, where each row
is sorted in non-decreasing order.

Find the first col with a 1.

To solve this problem, loop through rows 0 -> rows - 1,
for the first row, use binary search to find the leftmost 1, assign its location
to result. For second row, if M(1, result) is 1, binary search for the first
1 in the second row between (0, result), and set location to result.
Keep going for all columns
"""
