# O(n) time | O(n) space, where n is the length of the input array
def minHeightBst(array):
    return buildBST(None, array, 0, len(array) - 1)


def buildBST(rootNode, array, startIdx, endIdx):
    if endIdx < startIdx:
        return
        
    midIdx = (startIdx + endIdx) // 2
    newNode = BST(array[midIdx])

    if rootNode is None:
        rootNode = newNode
    else:
        if array[midIdx] < rootNode.value:
            rootNode.left = newNode
            rootNode = rootNode.left
        else:
            rootNode.right = newNode
            rootNode = rootNode.right

    buildBST(rootNode, array, startIdx, midIdx - 1)
    buildBST(rootNode, array, midIdx + 1, endIdx)

    return rootNode


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
