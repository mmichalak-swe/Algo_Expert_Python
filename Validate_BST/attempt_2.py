# O(n) time | O(d) space, where n is the number of nodes in the BST, and
# d is the depth (or height) of the BST
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validBSTHelper(tree, float("-inf"), float("inf"))


def validBSTHelper(currentNode, minValue, maxValue):
    if currentNode is None:
        return True

    if not (minValue <= currentNode.value < maxValue):
        return False
        
    left = validBSTHelper(currentNode.left, minValue, currentNode.value)
    return left and validBSTHelper(currentNode.right, currentNode.value, maxValue)
