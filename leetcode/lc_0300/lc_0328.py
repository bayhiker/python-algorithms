from typing import Optional
from lib.singly_linked_list import ListNode, get_linked_list, get_list


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.odd_even_list(head)

    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        curr_odd = head.next.next
        curr_even = head.next
        head_even = head.next
        head.next = curr_odd
        while True:
            if curr_odd.next is None:
                curr_odd.next = head_even
                curr_even.next = None
                break
            curr_even.next = curr_odd.next
            curr_even = curr_even.next
            if curr_even.next is None:
                curr_odd.next = head_even
                break
            curr_odd.next = curr_even.next
            curr_odd = curr_odd.next

        return head
