# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_linked_list(nodes: list[int]) -> ListNode:
    if not nodes:
        return None
    curr_node: ListNode = None
    head: ListNode = None
    for i in nodes:
        next_node = ListNode(i)
        if curr_node is None:
            curr_node = next_node
            head = curr_node
        else:
            curr_node.next = next_node
            curr_node = curr_node.next
    return head


def get_list(head: ListNode) -> list[int]:
    nodes = []
    curr_node = head
    while curr_node is not None:
        nodes.append(curr_node.val)
        curr_node = curr_node.next
    return nodes
