# O(n) time | O(log(n)) space, where n is the number of nodes in the tree
def maxPathSum(tree):
    mST = maxSumTriangle(float('-inf'))
    return maxPathSumHelper(tree, mST)


class maxSumTriangle:
    def __init__(self, maxSumTriangle):
        self.maxSumTriangle = maxSumTriangle


def maxPathSumHelper(tree, mST, root=True):
    if tree is None:
        return 0

    value = tree.value
    leftPathMaxSum = value + maxPathSumHelper(tree.left, mST, False)
    rightPathMaxSum = value + maxPathSumHelper(tree.right, mST, False)
    maxLeftRight = max(leftPathMaxSum, rightPathMaxSum)
    maxSumCurrentNode = leftPathMaxSum - value + rightPathMaxSum
    
    if root is True:
        return max(value, maxLeftRight, maxSumCurrentNode, mST.maxSumTriangle)
    else:
        mST.maxSumTriangle = max(mST.maxSumTriangle, maxLeftRight, maxSumCurrentNode)
        return max(value, maxLeftRight)
