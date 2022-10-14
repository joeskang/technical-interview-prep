# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node_dict = {}  # keys: Node.val, values: [Node]

        # aggregation phase
        while 1:
            has_node = False
            for i in range(len(lists)):
                node = lists[i]
                if node is not None and node.val is not None:
                    has_node = True
                    temp = node.next
                    node.next = None
                    node_dict[node.val] = [node] if node.val not in node_dict else node_dict[node.val] + [node]
                    lists[i] = temp

            if not has_node:
                break

        keys = list(node_dict.keys())
        keys.sort()

        root_node = head = ListNode(-1)

        for key in keys:
            for node in node_dict[key]:
                head.next = node
                head = head.next
        return root_node.next
