"""
completed previously (before June 26, 2022)
* likely around December 2021 or Jan 2022
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1 = []
        a2 = []
        while l1 is not None:
            a1.insert(0, l1.val)
            l1 = l1.next
        while l2 is not None:
            a2.insert(0, l2.val)
            l2 = l2.next

        carry = 0
        head = output = None
        while a1 or a2:
            left = 0 if not a1 else a1.pop()
            right = 0 if not a2 else a2.pop()
            sum_ = left + right + carry
            # output.append(sum_%10)
            if not output:
                head = output = ListNode(val=sum_ % 10)
            else:
                output.next = ListNode(val=sum_ % 10)
                output = output.next
            carry = sum_ // 10

        if carry:
            output.next = ListNode(val=carry)
            output = output.next

        return head
