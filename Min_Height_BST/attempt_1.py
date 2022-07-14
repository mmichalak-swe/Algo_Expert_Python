# O(n*log(n)) time | O(n) space, where n is the length of the input array
# time complexity: it takes log(n) time to insert something into a BST, we need to
# do that n times, thus n*log(n)
def minHeightBst(array):
    rootNode = BST(array[len(array) // 2])
    buildBST(rootNode, array, len(array) // 2)
    return rootNode


def buildBST(rootNode, array, rootIdx):
    leftSlice = array[:rootIdx]
    rightSlice = array[rootIdx+1:]

    if leftSlice:
        idx = getRootIdx(leftSlice)
        value = leftSlice[idx]
        rootNode.insert(value)
        buildBST(rootNode, leftSlice, idx)
    if rightSlice:
        idx = getRootIdx(rightSlice)
        value = rightSlice[idx]
        rootNode.insert(value)
        buildBST(rootNode, rightSlice, idx)


def getRootIdx(array):
    return len(array) // 2


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
