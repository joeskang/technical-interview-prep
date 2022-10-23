"""
partially completed previously (before Jun 26, 2022)
* likely around Dec 2021 or Jan 2022
* completed Jun 26, 2022
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = current = None

        while list1 is not None or list2 is not None:
            v1 = None if list1 is None else list1.val
            v2 = None if list2 is None else list2.val

            if v1 is not None and (v2 is None or v1 <= v2):
                if head is None:
                    head = current = ListNode(val=v1)
                else:
                    current.next = ListNode(val=v1)
                    current = current.next
                list1 = list1.next

            elif v2 is not None and (v1 is None or v2 < v1):
                if head is None:
                    head = current = ListNode(val=v2)
                else:
                    current.next = ListNode(val=v2)
                    current = current.next

                list2 = list2.next

        return head