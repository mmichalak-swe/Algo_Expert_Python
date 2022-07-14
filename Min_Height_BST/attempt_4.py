# O(n) time | O(n) space, where n is the length of the input array
def minHeightBst(array):
    return buildBST(None, array, 0, len(array) - 1)


def buildBST(tree, array, start, end):
    if start > end:
        return

    middle = (start + end) // 2
    value = array[middle]

    if tree is None:
        tree = BST(value)
    else:
        if value < tree.value:
            tree.left = BST(value)
            tree = tree.left
        else:
            tree.right = BST(value)
            tree = tree.right

    buildBST(tree, array, start, middle - 1)
    buildBST(tree, array, middle + 1, end)

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