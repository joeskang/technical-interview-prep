"""
Runtime: 30 ms, faster than 65.72% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.9 MB, less than 98.80% of Python3 online submissions for Middle of the Linked List.

Time: 19m 21s (12/7/21)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        """after testing, of course there isn't a length"""
        # convert list to array
        pointer = head
        node_count = 0
        while pointer.next:
            node_count += 1
            pointer = pointer.next

        half = node_count // 2
        # if even, take upper
        if node_count % 2:
            half += 1
        for i in range(half):
            head = head.next

        return head

        """I guess this is against the rules"""
        # midpoint = len(arr) // 2
        #
        # output = []
        # for i in range(midpoint, len(arr)):
        #     output.append(arr[i])
        #
        # return output


def test_solution():
    sol = Solution()
    assert sol.middleNode([1,2,3,4,5]) == [3,4,5]
    assert sol.middleNode([1,2,3,4,5,6]) == [4,5,6]

if __name__ == "__main__":
    test_solution()
