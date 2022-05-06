# O(n) time | O(h) space - where n is # of nodes, h is height of tree

def nodeDepths(root):
    depth = 0
    node = root
    return nodeDepthsHelper(node, depth)


def nodeDepthsHelper(node, depth):
    if not node:
        return 0
    
    if not node.left and not node.right:
        return depth

    return depth + nodeDepthsHelper(node.left, depth+1) + nodeDepthsHelper(node.right, depth+1)
    

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
