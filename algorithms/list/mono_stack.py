from collections import deque


class MonoStack:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        self.n = len(nums)

    def get_nexts(self, smaller=True, allow_equal=False):
        nexts: list[int] = [self.n] * self.n
        s = deque()

        for i, num in enumerate(self.nums):
            while len(s) > 0 and (
                (
                    smaller
                    and (
                        (top := self.nums[s[len(s) - 1]]) > num
                        or (top == num and allow_equal)
                    )
                )
                or (
                    not smaller
                    and (
                        (top := self.nums[s[len(s) - 1]]) < num
                        or (top == num and allow_equal)
                    )
                )
            ):
                nexts[s.pop()] = i
            s.append(i)
        return nexts


def test_mono_stack():
    ms = MonoStack([3, 7, 7, 6, 2])
    assert ms.get_nexts() == [4, 3, 3, 4, 5]
    assert ms.get_nexts(allow_equal=True) == [4, 2, 3, 4, 5]
    assert ms.get_nexts(smaller=False) == [1, 5, 5, 5, 5]
    assert ms.get_nexts(smaller=False, allow_equal=True) == [1, 2, 5, 5, 5]
