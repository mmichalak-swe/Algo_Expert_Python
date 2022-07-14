# O(n) time | O(n) space, where n is the length of the input array
# time worst than O(n) due to slicing
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
        rootNode.left = BST(value)
        buildBST(rootNode.left, leftSlice, idx)
    if rightSlice:
        idx = getRootIdx(rightSlice)
        value = rightSlice[idx]
        rootNode.right = BST(value)
        buildBST(rootNode.right, rightSlice, idx)


def getRootIdx(array):
    return len(array) // 2


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def insert(self, value):
    #     if value < self.value:
    #         if self.left is None:
    #             self.left = BST(value)
    #         else:
    #             self.left.insert(value)
    #     else:
    #         if self.right is None:
    #             self.right = BST(value)
    #         else:
    #             self.right.insert(value)
