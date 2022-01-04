"""
Runtime: 52 ms, faster than 54.50% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15 MB, less than 99.29% of Python3 online submissions for Reverse Nodes in k-Group.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):

        prehead = ListNode(-1)
        prehead.next = head

        current = prehead
        while current:
            precur = current
            current = current.next

            cache = []
            for i in range(k):
                if not current:
                    return prehead.next
                cache.append(current)
                current = current.next

            remainder = current
            # remainder = current.next if current else None
            current = precur

            while cache:
                insert_node = cache.pop()
                current.next = insert_node
                current = current.next

            current.next = remainder

        return prehead.next


l1 = [1,2,3,4,5]
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
x = sol.reverseKGroup(LIST1, 2)
pass
