class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        return self.find_original_array_deque(changed)

    def find_original_array_deque(self, changed: list[int]) -> list[int]:
        # Use a deque to store expected 2x of original arr,
        # Once we actually see that 2x in changed, add x to result,
        # If changed is empty while deque is not, then what ever is left
        # in dq has no corresponding num in original array

        orig_arr = []
        from collections import deque

        dq = deque()
        for num in sorted(changed):
            if dq and num == dq[0]:
                dq.popleft()
            else:
                dq.append(num * 2)
                orig_arr.append(num)
        return orig_arr if not dq else []

    def find_original_array_hash(self, changed: list[int]) -> list[int]:
        # d[i] True, i is in changed
        # for any i,
        #     if i is odd, if d[2*i], then add i to result, else return []
        #     if i is even, lookup d[2*i] and d[i//2], if non exist return [],
        #          if only d[i//2] exists, add i//2 to result,
        #          if only d[2 ** i] exists, add i to result
        #          if both exist, try to expand left (//2) and right (*2) as much as possible,
        #               if odd number of items in this expanded list, then return [],
        #               if even number of items in this expanded list, then add the 0th,2nd, 4th, .. to result
        #

        pass
