"""
started: June 28, 2022

status: completed June 28, 2022
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recursive_validate(node, low=-math.inf, high=math.inf):

            # handle empty node
            if not node:
                return True

            if (value := node.val) <= low or value >= high:
                return False

            return recursive_validate(node.left, low, node.val) and recursive_validate(node.right, node.val, high)

        return recursive_validate(root)