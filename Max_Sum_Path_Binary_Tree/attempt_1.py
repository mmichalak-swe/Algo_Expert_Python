# O(n) time | O(log(n)) space, where n is the number of nodes in the tree
def maxPathSum(tree):
    pSC = pathSumCurrent(float('-inf'))
    return maxPathSumHelper(tree, pSC)


class pathSumCurrent:
    def __init__(self, maxSumWithNode):
        self.maxSumWithNode = maxSumWithNode


def maxPathSumHelper(tree, pSC, root=True):
    if tree is None:
        return 0

    leftPathSum = tree.value + maxPathSumHelper(tree.left, pSC, False)
    rightPathSum = tree.value + maxPathSumHelper(tree.right, pSC, False)
    
    if root is True:
        return max(tree.value, leftPathSum, rightPathSum, leftPathSum - tree.value + rightPathSum, pSC.maxSumWithNode)
    else:
        pSC.maxSumWithNode = max(pSC.maxSumWithNode, leftPathSum, rightPathSum, leftPathSum - tree.value + rightPathSum)
        return max(tree.value, leftPathSum, rightPathSum)
