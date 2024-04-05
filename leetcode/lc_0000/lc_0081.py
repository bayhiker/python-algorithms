class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        return self.search_iterative(nums, target)

    def search_recursive(self, nums: list[int], target: int) -> bool:
        def find_target(left, right) -> bool:
            nonlocal nums, target
            if left > right:
                return False
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    return find_target(left, mid - 1)
                else:
                    return find_target(mid + 1, right)
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    return find_target(mid + 1, right)
                else:
                    return find_target(left, mid - 1)
            if nums[mid] < nums[left]:
                # Pivot on the left, right half is constant
                return find_target(left, mid - 1)
            if nums[mid] > nums[right]:
                # Pivot on the right, right half is constant
                return find_target(mid + 1, right)
            # left == right == mid,
            # could be left: 123111111111, or right 11111111112311
            return find_target(left, mid - 1) or find_target(mid + 1, right)

        return find_target(0, len(nums) - 1)

    def search_iterative(self, nums: list[int], target: int) -> bool:
        # Use updated binary sort:
        # nums: 2,5,6,0,0,1,2 mid is 0, since 0 is less than or equal to nums[6],
        # there for the right side is sorted.
        # In other cases, if 0 is larger than or equal to nums[0], then the left is sorted
        right, left = len(nums) - 1, 0
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target:
                return True
            go_left = True
            if nums[mid] > nums[left]:
                # The left half is sorted
                go_left = target >= nums[left] and target < nums[mid]
            elif nums[mid] < nums[right]:
                # The right half is sorted
                go_left = not (target > nums[mid] and target <= nums[right])
            elif nums[mid] < nums[left]:
                # Pivot on the left, right half is constant
                go_left = True
            elif nums[mid] > nums[right]:
                # Pivot on the right, left half is constant
                go_left = False
            else:
                # left == right == mid,
                left, right = left + 1, right - 1
                continue
            if go_left:
                right = mid - 1
            else:
                left = mid + 1

        return False
