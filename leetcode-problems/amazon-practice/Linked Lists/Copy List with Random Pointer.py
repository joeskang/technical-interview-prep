"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #         prehead = Node(-1)
        #         prehead.next = head
        #         node_list = []

        #         while head is not None:
        #             node_list.append(Node(head.val))
        #             head = head.next

        #         head = prehead.next
        #         pre_results = Node(-1)
        #         pre_results.next = node_list[0]
        #         for node in node_list:
        #             if head.random is not None:
        #                 node.random = node_list[head.random]
        #             if head.next is not None:
        #                 node.next = node_list[head.next]

        #         return pre_results.next

        prehead = Node(-1)
        prehead.next = head
        orig_node_dict = {}  # keys: memory location, values: [node.val, node.next, node.random]
        new_node_dict = {}

        while head is not None:
            orig_node_dict[id(head)] = [head.val, id(head.next), id(head.random)]
            new_node = Node(-1)
            new_node_dict
