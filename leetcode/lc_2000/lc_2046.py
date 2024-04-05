from typing import Optional
from lib.singly_linked_list import ListNode


class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sort_linked_list(head)

    def sort_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Observation 1: all positive nodes are already ordered.
        # Observation 2: all negative nodes are ordered in non-increasing order
        # So start from head, go through all nodes, once you see a negative
        # node, move it to the left most location, and move head to point to
        # current negative node.
        pass
