"""
June 28, 2022
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_list = [root]
        values_list = []

        # generational loop
        while node_list:
            temp_nodes = []
            generation_values = []

            # left to right loop
            for node in node_list:
                # will assume that null check was already performed
                generation_values.append(node.val)

                if node.left:
                    temp_nodes.append(node.left)
                if node.right:
                    temp_nodes.append(node.right)
            node_list = temp_nodes
            if generation_values:
                values_list += [generation_values]
        return values_list