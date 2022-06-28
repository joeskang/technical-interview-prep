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
        # node emulation with dictionary
        orig_node_dict = {}  # keys: memory location, values: [node.val, node.next, node.random]
        new_node_dict = {}
        new_root = Node(-1)
        new_head = None

        # copy nodes with orig_node_dict
        while head is not None:
            next_ = head.next
            random_ = head.random
            orig_node_dict[id(head)] = [head.val, id(next_) if next_ is not None else None,
                                        id(random_) if random_ is not None else None]
            new_node = Node(-1)
            new_node_dict[id(head)] = new_node
            head = head.next

        head = prehead.next
        # assign next and random
        while head is not None:

            new_head = new_node_dict[id(head)]

            if new_root.next is None:
                new_root.next = new_head
            # get next from old to refer to new
            val, next_, random_ = orig_node_dict[id(head)]
            new_head.val = val
            new_head.next = new_node_dict[next_] if next_ is not None else None
            new_head.random = new_node_dict[random_] if random_ is not None else None
            head = head.next

        return new_root.next
