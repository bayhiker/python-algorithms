from typing import Dict, List

# 2-Sum
# Find the two nums[i] such that they add up to target
#
# Constraints:
# - 2 <= len(nums) <= 10**4
# - -10**9 <= nums[i] <= 10**9
# - -10**9 <= target <= 10**9
# - There's exactly one solution
# - The same element cannot be used twice
#
# leetcode_1
def two_sum(nums: List[int], target: int) -> List[int]:
    # h[k] = v
    h: Dict[int, List[int]] = {}
    for i in range(len(nums)):
        num = nums[i]
        if num not in h:
            h[num] = [i]
        else:
            h[num].append(i)
    for num in nums:
        if num == target / 2 and len(h[num]) >= 2:
            return [h[num][0], h[num][1]]
        if num != target / 2 and target - num in h:
            return [h[num][0], h[target - num][0]]
    return None


# Two Sun iii
#
# Design and implement a Two Sum class with two operations
# - add(i) adds i to an internal data structure
# - find(s): find if there exists any pair of numbers whose sum is equal to s
#
#
# Two approaches:
# Approach 1: add O(n) and find O(1), use two hashes:
# (1) occurrences, key is i, value is number of times i is added
# (2) sum_pairs, key is sum, value is a list of pairs adding up to that sum
# Approach 2: add O(1) and find O(n), similar to 2-sum above, use one hashtable occurrences
# leetcode_170


def test_two_sum() -> None:
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
