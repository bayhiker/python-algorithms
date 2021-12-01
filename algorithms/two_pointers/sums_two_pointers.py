# Some sum problems are under "dynamic programming"
from typing import List, Optional
import sys
import numpy

from algorithms.lib.bst import TreeNode, bst2inorder, preorder2bst

# 3sum:
# Given integer array nums, return all triplets [nums[i], nums[j], nums[k]]
# s.t. i != j, j!=k, and k!=i
#
# Constraints:
# - 0<= len(nums) <= 3000
# - -10**5 <= nums[i] <= 10**5
# leetcode_15
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    valid_combos: List[List[int]] = []
    i = 0
    while i < n:
        p1, p2 = i + 1, n - 1
        while p1 < p2:
            current_sum = nums[i] + nums[p1] + nums[p2]
            move_p1, move_p2 = False, False
            if current_sum == 0:
                valid_combos.append([nums[i], nums[p1], nums[p2]])
                move_p1, move_p2 = True, True
            elif current_sum < 0:
                move_p1 = True
            else:
                move_p2 = True
            if move_p1:
                while p1 < n - 1 and nums[p1 + 1] == nums[p1]:
                    p1 += 1
                p1 += 1
            if move_p2:
                while p2 > 0 and nums[p2 - 1] == nums[p2]:
                    p2 -= 1
                p2 -= 1
        # Skip duplicate numbers
        while i < n - 1 and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return valid_combos


# 3Sum Closest:
# Given nums of length n, and an integer target, find the sum of three integers in nums
# where sum is closest to target.
#
# leetcode_16
def three_sum_closest(nums: List[int], target: int) -> int:
    n = len(nums)
    nums.sort()
    closest_sum = sys.maxsize
    for i in range(n):
        p1, p2 = i + 1, n - 1
        while p1 < p2:
            current_sum = nums[i] + nums[p1] + nums[p2]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum == target:
                return current_sum
            elif current_sum > target:
                p2 -= 1
            else:
                p1 += 1
    return closest_sum


# Two Sum ii: input array is sorted
# numbers[i] is a 1-indexed sorted in non-decreasing order, find two numbers
# with index x1 and x2 s.t. 1<= x1 < x2 < len(numbers)
#
# leetcode_167
def two_sum_ii(numbers: List[int], target: int) -> List[int]:
    p1, p2 = 1, len(numbers)
    while p1 < p2:
        current_sum = numbers[p1 - 1] + numbers[p2 - 1]
        if current_sum == target:
            return [p1, p2]
        elif current_sum < target:
            p1 += 1
        else:
            p2 -= 1
    return None


# Two Sum iv - Input is a BST
# Given root of a BST and target number k, return if there exists two elements in the BST
# s.t. they add up to k
#
# leetcode_653
def two_sum_iv(root: Optional[TreeNode], k: int) -> bool:
    nums: List[int] = bst2inorder(root)
    p1, p2 = 0, len(nums) - 1
    while p1 < p2:
        if nums[p1] + nums[p2] == k:
            return True
        elif nums[p1] + nums[p2] < k:
            p1 += 1
        else:
            p2 -= 1
    return False


# Two sum less then k:
# Find max sum S of two numbers in integer array A s.t. S is no more than
# given number K
#
# Constraints:
# - 1 <= len(A) <= 100
# - 1 <= A[i] <= 1000
# - 1 <= K <= 2000
#
# leetcode_1099
def two_sum_less_than_k(A: List[int], K) -> int:
    A.sort()
    p1, p2 = 0, len(A) - 1
    max_sum = -sys.maxsize
    while p1 < p2:
        current_sum = A[p1] + A[p2]
        if current_sum == K:
            max_sum = K
            break
        elif current_sum < K:
            max_sum = current_sum
            p1 += 1
        else:
            p2 -= 1
    return None if max_sum == -sys.maxsize else max_sum


# Two Sum BSTs
# Given two BSTs, return true if and only if there's node in the first tree
# and a node in the second tree that add up to target
#
# Constraints
# - Each tree has no more than 5k nodes
# - -10**9 <= target, node.val <= 10**9
#
# leetcode_1150
def two_sum_bsts(root1: TreeNode, root2: TreeNode, target: int) -> bool:
    nums1 = bst2inorder(root1)
    n1 = len(nums1)
    nums2 = bst2inorder(root2)
    n2 = len(nums2)
    p1, p2 = 0, n2 - 1
    while p1 < n1 and p2 >= 0:
        current_sum = nums1[p1] + nums2[p2]
        if current_sum == target:
            return True
        elif current_sum < target:
            p1 += 1
        else:
            p2 -= 1
    return False


# 4sum:
# nums of n integers, find all unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
# such that: 0<=a,b,c,d<n, a/b/c/d are distinct, sum(nums[a,b,c,d]) = target
#
# Constraints:
#    - 1 <= len[nums] <= 200
#    - -10**9 <= nums[i] <= 10**9
#    - -10**9 <= target <= 10**9
#
# Key to solving 4sum: for any fixed nums[p1], this becomes a 3sum(nums[p1+1, n-1], target-nums[-1])
# Time O(n**3), space O(n)
def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    valid_combos: List[List[int]] = []
    if n < 4:
        return valid_combos
    p1 = 0
    while p1 < n - 3:
        p2 = p1 + 1
        while p2 < n - 2:
            p3, p4 = p2 + 1, n - 1
            while p4 > p3:
                move_p3, move_p4 = False, False
                current_combo = [nums[p1], nums[p2], nums[p3], nums[p4]]
                current_sum = sum(current_combo)
                if current_sum == target:
                    valid_combos.append(current_combo)
                    move_p2, move_p3 = True, True
                elif current_sum < target:
                    move_p3 = True
                else:
                    move_p4 = True
                if move_p3:
                    while p3 < p4 and nums[p3 + 1] == nums[p3]:
                        p3 += 1
                    p3 += 1
                if move_p4:
                    while p4 > p3 and nums[p4 - 1] == nums[p4]:
                        p4 -= 1
                    p4 -= 1
            while p2 < n - 2 and nums[p2 + 1] == nums[p2]:
                p2 += 1
            p2 += 1
        while p1 < n - 3 and nums[p1 + 1] == nums[p1]:
            p1 += 1
        p1 += 1
    return valid_combos


def test_two_sum_ii() -> None:
    assert two_sum_ii([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_ii([2, 3, 4], 6) == [1, 3]
    assert two_sum_ii([-1, 0], -1) == [1, 2]


def test_two_sum_less_than_k() -> None:
    assert two_sum_less_than_k([1, 4, 2, 3], 7) == 7


def test_two_sum_iv() -> None:
    assert two_sum_iv(preorder2bst([5, 3, 6, 2, 4, None, 7]), 9)
    assert not two_sum_iv(preorder2bst([5, 3, 6, 2, 4, None, 7]), 28)
    assert two_sum_iv(preorder2bst([2, 1, 3]), 4)
    assert not two_sum_iv(preorder2bst([2, 1, 3]), 1)


def test_two_sum_bsts() -> None:
    assert two_sum_bsts(preorder2bst([2, 1, 4]), preorder2bst([1, 0, 3]), 5)
    assert not two_sum_bsts(
        preorder2bst([0, -10, 10]), preorder2bst([5, 1, 7, 0, 2]), 18
    )


def test_three_sum() -> None:
    assert len(three_sum([])) == 0
    assert len(three_sum([0])) == 0
    assert numpy.array_equal(
        numpy.array(three_sum([0, 0, 0, 0])),
        numpy.array([[0, 0, 0]]),
    )
    assert numpy.array_equal(
        numpy.array(three_sum([-1, 0, 1, 2, -1, -4])),
        numpy.array([[-1, -1, 2], [-1, 0, 1]]),
    )
    assert numpy.array_equal(
        numpy.array(three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])),
        numpy.array(
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
        ),
    )


def test_three_sum_closest() -> None:
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2
    assert three_sum_closest(nums=[0, 0, 0], target=1) == 0


def test_four_sum() -> None:
    assert numpy.array_equal(
        numpy.array(four_sum([1, 0, -1, 0, -2, 2], 0)),
        numpy.array(
            [
                [-2, -1, 1, 2],
                [-2, 0, 0, 2],
                [-1, 0, 0, 1],
            ]
        ),
    )
    assert numpy.array_equal(
        numpy.array(four_sum([2, 2, 2, 2, 2], 8)),
        numpy.array(
            [
                [2, 2, 2, 2],
            ]
        ),
    )
    assert numpy.array_equal(
        numpy.array(four_sum([-2, -1, -1, 1, 1, 2, 2], 0)),
        numpy.array(
            [
                [-2, -1, 1, 2],
                [-1, -1, 1, 1],
            ]
        ),
    )
    assert numpy.array_equal(
        numpy.array(four_sum([-3, -1, 0, 2, 4, 5], 2)),
        numpy.array(
            [
                [-3, -1, 2, 4],
            ]
        ),
    )
