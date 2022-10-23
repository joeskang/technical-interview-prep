class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root_node = pre_curr = ListNode()
        root_node.next = head

        selected_nodes = []

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

        # handle the last node
        if curr_count == k:
            while selected_nodes:
                curr = selected_nodes.pop()
                pre_curr.next = curr
                pre_curr = curr
        else:
            for node in selected_nodes:
                pre_curr.next = node
                pre_curr = node

        return root_node.next


def make_test_case():
    root = head = ListNode()
    for i in range(5):
        new_node = ListNode()
        new_node.val = i + 1
        head.next = new_node
        head = new_node
    return root.next

if __name__ == "__main__":
    test_list = make_test_case()
    sol = Solution()
    my_list = sol.reverseKGroup(test_list, 2)
