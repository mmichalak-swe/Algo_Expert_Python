# O(n) time | O(n) space, where n is the length of the input array
def minHeightBst(array):
    return buildBST(array, 0, len(array) - 1)


def buildBST(array, start, end):
    if start > end:
        return None

    middle = (start + end) // 2
    tree = BST(array[middle])
    tree.left = buildBST(array, start, middle - 1)
    tree.right = buildBST(array, middle + 1, end)
    return tree


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