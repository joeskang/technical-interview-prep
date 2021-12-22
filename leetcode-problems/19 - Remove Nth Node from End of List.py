"""
Runtime: 38 ms, faster than 26.29% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.1 MB, less than 92.40% of Python3 online submissions for Remove Nth Node From End of List.
"""

class Optional:
    def __init__(self, nums):
        head = ListNode(val=nums[0])
        pointer = head
        for i in range(1,len(nums)):
            num = nums[i]
            pointer.next = ListNode(val=num)
            pointer = pointer.next
        self.head = head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        foot = head

        node_count = 1
        while foot.next:
            foot = foot.next
            node_count += 1

        if node_count - n == 0:
            return head.next
        pointer = head
        pointer_next = pointer.next.next

        for i in range(1, node_count - n ):
            pointer = pointer.next
            pointer_next = pointer.next.next

        pointer.next = pointer_next

        return head


def test_solution():
    opt = Optional([1,2,3,4,5]).head
    sol = Solution()
    temp = sol.removeNthFromEnd(opt, 2)
    pass

