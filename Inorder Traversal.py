You have been given a Binary Tree of 'n' nodes, where the nodes have integer values. Your task is to return the In-Order traversal of the given binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(root):
    result = []
    in_order_helper(root, result)
    return result

def in_order_helper(node, result):
    if node is None:
        return
    in_order_helper(node.left, result)
    result.append(node.val)
    in_order_helper(node.right, result)

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    in_order = in_order_traversal(root)
    print("In-Order Traversal:", in_order)
