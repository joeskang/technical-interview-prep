'''
Runtime: 1267 ms, faster than 6.79% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 47.5 MB, less than 17.23% of Python3 online submissions for Palindrome Linked List.
'''


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get length
        length = 0
        prenode = ListNode(-1)
        prenode.next = head
        values = []

        while head:
            values.append(head.val)
            head = head.next

        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1

        return True