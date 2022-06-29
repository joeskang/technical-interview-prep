"""
started: June 28, 2022

status: in progress
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        is_valid = True
        # use bfs
        # bfs uses queues, dfs uses stacks

        # the first node check will be used to populate node_list
        # check left

        node_list = [root]

        while node_list:
            if (left_node := root.left) is not None:
                if left_node.val < root.val:
                    node_list.append(left_node)
                else:
                    return False

            if (right_node := root.right) is not None:
                if right_node.val > root.val:
                    node_list.append(right_node)
                else:
                    return False
            root = node_list[0]
            node_list = node_list[1:]
        return True

        # don't need to preserve root, will use it to traverse graph