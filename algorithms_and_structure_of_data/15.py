class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
    
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    
    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

invertTree(root)