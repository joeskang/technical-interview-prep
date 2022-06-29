# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        node_list = [root]
        values_list = []
        left_to_right = False  # the first generation is right to left

        # generational loop
        while node_list:

            temp_nodes = []
            generation_values = []

            # left to right or right to left loop

            for i in range(len(node_list)):
                node = node_list[i] if left_to_right else node_list[len(node_list) - 1 - i]
                if node:
                    generation_values.append(node.val)
                    # FILO if right_to_left
                    # FIFO if left_to_right
                    if left_to_right:

                        if node.left:
                            temp_nodes.append(node.left)
                        if node.right:
                            temp_nodes.append(node.right)
                    else:
                        if node.right:
                            temp_nodes.append(node.right)
                        if node.left:
                            temp_nodes.append(node.left)

            if not left_to_right:
                temp_nodes = temp_nodes[::-1]
                generation_values = generation_values[::-1]

            left_to_right = not left_to_right
            node_list = temp_nodes
            values_list += [generation_values]
        return values_list


if __name__ == "__main__":
    sol = Solution()
    mytree_root = TreeNode(3)
    mytree_root.left = TreeNode(9)
    mytree_root.right = TreeNode(20)
    mytree_root.right.left = TreeNode(15)
    mytree_root.right.right = TreeNode(7)

    response = sol.zigzagLevelOrder(mytree_root)
    pass
