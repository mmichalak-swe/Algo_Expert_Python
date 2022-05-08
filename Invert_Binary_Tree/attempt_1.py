# O(n) time | O(h) space

def invertBinaryTree(tree):
    if not tree:
        return
    swapTree(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapTree(node):
    node.left, node.right = node.right, node.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
