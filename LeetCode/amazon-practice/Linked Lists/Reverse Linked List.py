# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_root = ListNode(-1)

        while head is not None:
            temp = head.next
            head.next = node_root.next
            node_root.next = head
            head = temp
        return node_root.next