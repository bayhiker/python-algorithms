from typing import Optional
from lib.singly_linked_list import ListNode


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        return self.get_intersection_node(headA, headB)

    """
    Suppose head_a and head_b meet at node_common,
    Distance from head_a to node_common is L1
    Distance from head_b to node_common is L2
    node_common to shared linked list end is L3

    Traverse from head_a to end of linked list, then start from head_b traverse L2 steps,
    you reach node_common. Total steps L1+L3+L2
    Traverse from head_b to end of linked list, then start from head_a traverse L1 steps,
    you reach node_common. Total steps L2+L3+L1

    Note that the two uses the same number of steps to reach node_common.
    """

    def get_intersection_node(
        self, head_a: ListNode, head_b: ListNode
    ) -> Optional[ListNode]:
        a = head_a
        b = head_b
        while a is not b:
            a = a.next if a is not None else head_b
            b = b.next if b is not None else head_a
        return a
