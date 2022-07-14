# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(h + k) time | O(h) space, where h is the height of the BST
# must go all the way down before visiting any nodes, thus h time + k
def findKthLargestValueInBst(tree, k):
    global count
    count = 0
    global value
    value = None
    findKthHelper(tree, k)
    return value


def findKthHelper(tree, k, stop=False):
    global count
    global value

    if tree is None or stop is True:
        return

    findKthHelper(tree.right, k, stop)

    if count >= k:
        return

    count += 1
    if count == k:
        stop = True
        value = tree.value
        return value

    findKthHelper(tree.left, k, stop)
