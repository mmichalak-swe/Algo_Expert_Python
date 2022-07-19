# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(h) time | O(h) space, where h is the height of the BST
# h space due to recursive calls on the call stack
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDescendant(nodeTwo, nodeThree):
        if isDescendant(nodeOne, nodeTwo):
            return True

    elif isDescendant(nodeTwo, nodeOne):
        if isDescendant(nodeThree, nodeTwo):
            return True

    return False


def isDescendant(parent, target):
    if parent is None:
        return False

    if parent.value > target.value:
        parent = parent.left
    elif parent.value < target.value:
        parent = parent.right
    else:
        # parent = target
        return True

    return isDescendant(parent, target)
