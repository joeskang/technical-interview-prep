"""Runtime: 109 ms, faster than 5.26% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.2 MB, less than 26.47% of Python3 online submissions for Remove Linked List Elements."""


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        prehead = ListNode(-1)
        prehead.next = head
        prev = prehead

        while head:
            if head.val == val:
                prev.next = head.next
                # head = head.next

            else:

                prev = head
            head = head.next

        return prehead.next