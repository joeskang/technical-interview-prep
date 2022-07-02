"""
Runtime: 60 ms, faster than 7.90% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 15.1 MB, less than 43.99% of Python3 online submissions for Copy List with Random Pointer.
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_prehead = Node(-1)
        old_node_indices = {}
        old_random = {}

        # traverse the original and get the indices
        old_prehead.next = head
        new_prehead = Node(-1)
        new_prehead.next = new_head = None

        new_nodes = []

        index = 0
        while head:
            old_node_indices[id(head)] = index
            old_random[id(head)] = id(head.random)

            index += 1
            new_node = Node(x=head.val)


            if new_prehead.next is None:
                new_prehead.next = new_head = new_node
            else:
                new_head.next = new_node
                new_head = new_head.next

            new_nodes.append(new_node)
            head = head.next

        head = old_prehead.next
        new_head = new_prehead.next
        while head:
            # print(head.random)
            if head.random:
                index = old_node_indices[id(head.random)]
                new_head.random = new_nodes[index]
            else:
                new_head.random = None
            new_head = new_head.next
            head = head.next

        return new_prehead.next