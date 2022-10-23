""" not my solution 6/29/2022 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def find_max(node):
            nonlocal max_sum

            if not node:
                return 0

            left_gain = max(find_max(node.left), 0)
            right_gain = max(find_max(node.right), 0)

            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)

            # if this price_newpath is worth it, then the max function should return it
            return node.val + max(left_gain, right_gain)

        max_sum = -math.inf
        find_max(root)
        return max_sum