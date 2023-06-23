
class TreeNode:
    def __init__(self, val: int = None):
        self.val = val
        self.left = None
        self.right = None

def search(root, target):

    # edge case or base case
    if not root:
        return False

    if target > root.val:
        search(root.right, target)

    elif target < root.val:
        search(root.left, target)


    else:
        return True