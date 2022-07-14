# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(n) space, where n is the number of nodes in the tree
def findKthLargestValueInBst(tree, k):
    sortedOrder = []
    buildOrder(tree, sortedOrder)
    return sortedOrder[k-1]


def buildOrder(tree, order):
    if tree is None:
        return

    buildOrder(tree.right, order)
    order.append(tree.value)
    buildOrder(tree.left, order)
