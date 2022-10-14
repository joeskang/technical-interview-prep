# TODO: finish this
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        before_head = ListNode(-1)
        current = before_head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        # returning head
        return before_head.next



l1 = [1,2,4]
l2 = [1,3,4]

LIST1 = ListNode(val=l1[0])
LIST2 = ListNode(val=l2[0])
preLIST1 = ListNode(-1)
preLIST1.next = LIST1

preLIST2 = ListNode(-1)
preLIST2.next = LIST2
for num in l1:
    LIST1.next = ListNode(val=num)
    LIST1 = LIST1.next

for num in l2:
    LIST2.next = ListNode(val=num)
    LIST2 = LIST2.next

LIST1 = preLIST1.next
LIST2 = preLIST2.next

sol = Solution()
print(sol.mergeTwoLists(LIST1, LIST2))