# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, numNodesVisited, lastValue):
        self.numNodesVisited = numNodesVisited
        self.lastValue = lastValue


# O(h + k) time | O(h) space, where h is the height of the BST
# must go all the way down before visiting any nodes, thus h time + k
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    findKthHelper(tree, k, treeInfo)
    return treeInfo.lastValue


def findKthHelper(tree, k, treeInfo):
    if tree is None or treeInfo.numNodesVisited >= k:
        return

    findKthHelper(tree.right, k, treeInfo)

    if treeInfo.numNodesVisited == k:
        return

    treeInfo.numNodesVisited += 1
    treeInfo.lastValue = tree.value
    
    findKthHelper(tree.left, k, treeInfo)
