# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from lib.singly_linked_list import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Use Floyd's Circle Detection algorithm to find mid of list
        # Change direction of the second half,
        # Check palindrome
        # If needed, restore links of the second half
        pass
