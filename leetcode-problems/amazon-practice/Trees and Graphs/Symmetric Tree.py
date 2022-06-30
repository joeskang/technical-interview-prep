# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        # handle null edgecase
        if not root:
            return True

        # can we use recursion?
        def validate(left_node, right_node):
            if left_node is None and right_node is None:
                return True
            if (left_node is None and right_node is not None) or (left_node is not None and right_node is None):
                return False
            if left_node.val != right_node.val:
                return False
            return validate(left_node.left, right_node.right) and validate(left_node.right, right_node.left)

        return validate(root.left, root.right)

if __name__ == "__main__":
    mytree = TreeNode(1)
    mytree.left = TreeNode(2)
    mytree.right = TreeNode(2)
    mytree.left.left = TreeNode(3)
    mytree.left.right = TreeNode(4)
    mytree.right.left = TreeNode(4)
    mytree.right.right = TreeNode(3)
    sol = Solution()
    response = sol.isSymmetric(mytree)
    pass

