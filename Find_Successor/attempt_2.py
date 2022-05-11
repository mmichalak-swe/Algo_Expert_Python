# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right:
        return getLeftmostChild(node.right)

    return getRightmostParent(node)


def getLeftmostChild(node):
    currentNode = node

    while currentNode.left:
        currentNode = currentNode.left
        
    return currentNode

def getRightmostParent(node):
    currentNode = node
    
    while currentNode.parent and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    
    return currentNode.parent

