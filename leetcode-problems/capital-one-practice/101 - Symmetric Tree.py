"""
Runtime: 37 ms, faster than 24.76% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.4 MB, less than 51.41% of Python3 online submissions for Symmetric Tree.
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # bfs
        # left, right = root.left, root.right
        generation = [root.left, root.right]
        stack = []

        has_node = True
        while has_node:
            l, r = 0, len(generation) - 1
            new_left = []
            new_right = []
            has_node = False
            while l < r:

                left = generation[l]
                right = generation[r]
                if left or right:
                    has_node = True

                if (not left and right) or (left and not right):
                    return False

                if left and right:
                    if left.val != right.val:
                        return False

                    new_left.insert(0, left.right)
                    new_left.insert(0, left.left)
                    new_right.append(right.left)
                    new_right.append(right.right)

                l += 1
                r -= 1

            generation = new_left + new_right

        return True