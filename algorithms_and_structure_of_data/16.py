class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    if not node:
        return True
    
    if not(min_value < node.value < max_value):
        return False
    
    return (is_bst(node.left, min_value, node.value) and
            is_bst(node.right, node.value, max_value))
    
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

print(is_bst(root))