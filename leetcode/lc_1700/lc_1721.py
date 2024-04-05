from typing import Optional
from lib.singly_linked_list import ListNode


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.swap_nodes_swap_values(head, k)

    def swap_nodes_swap_values(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        fast = head
        for _ in range(k - 1):
            fast = fast.next
        p = fast
        slow = head
        while fast.next:
            slow, fast = slow.next, fast.next
        q = slow
        p.val, q.val = q.val, p.val
        return head

    def swap_nodes_swap_nodes(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        if head.next is None:
            # Only one element, return the list
            return head
        if head.next.next is None:
            # Only two elements, return swapped list
            head.next.next = head
            head = head.next
            head.next.next = None
            return head

        # p1 and p2 both point to head, p2 starts moving k steps first, this is
        p1, p2, p2_prev = head, head, None
        for i in range(1, k):
            p2_prev = p2
            p2 = p2.next
        pk, pk_prev = p2, p2_prev
        p1_prev = None
        while p2.next is not None:
            p1_prev = p1
            p1, p2 = p1.next, p2.next
        # Now pk points to kth from left, p1 points to kth from right, swap them
        if pk == head:  # k == 1 or n, and pk_prev == None
            head = p1
            p1.next = pk.next
            p1_prev.next = pk
            pk.next = None
        elif p1 == head:
            head = pk
            pk.next = p1.next
            pk_prev.next = p1
            p1.next = None
        else:
            pk_prev.next = p1
            p1_prev.next = pk
            pk_next = pk.next
            pk.next = p1.next
            p1.next = pk_next

        return head
