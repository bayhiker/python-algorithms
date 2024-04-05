# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from lib.singly_linked_list import ListNode
from typing import Optional


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        return self.nodes_between_critical_points(head)

    def nodes_between_critical_points(self, head: Optional[ListNode]) -> list[int]:
        p = head
        first_cp, last_cp, prev_cp = -1, -1, -1
        dist_min = 10**6
        counter = 0
        while p.next:
            if (
                p.next.next
                and (p.next.val - p.val) * (p.next.val - p.next.next.val) > 0
            ):
                if first_cp == -1:
                    first_cp, last_cp, prev_cp = counter, counter, counter
                else:
                    last_cp = counter
                    dist_min = min(dist_min, counter - prev_cp)
                    prev_cp = counter
            counter += 1
            p = p.next
        return [dist_min, last_cp - first_cp] if first_cp < last_cp else [-1, -1]
