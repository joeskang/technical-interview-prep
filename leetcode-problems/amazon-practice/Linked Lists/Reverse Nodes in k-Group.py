"""
Date started: Jun 26, 2022

status: incomplete
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root_node = ListNode()
        root_node.next = head

        selected_nodes = []

        pre_curr = ListNode()
        pre_curr.next = head
        post_curr = None

        curr_count = k
        while head is not None:
            post_curr = head.next

            # insert node and sever next
            if curr_count > 0:

                head.next = None
                selected_nodes.append(head)
                head = post_curr
                curr_count -= 1


            # re-arrangement sequence
            else:
                curr_count = k
                while selected_nodes:
                    curr = selected_nodes.pop()
                    pre_curr.next = curr
                    pre_curr = curr
                pre_curr.next = head

            selected_nodes.append()