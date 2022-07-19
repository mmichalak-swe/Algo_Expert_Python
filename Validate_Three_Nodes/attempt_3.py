# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(h) time | O(h) space, where h is the height of the BST
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    return validateThreeNodesHelper(nodeOne, nodeTwo, nodeThree, nodeOne) or validateThreeNodesHelper(nodeThree, nodeTwo, nodeOne, nodeThree)


def validateThreeNodesHelper(grandparent, parent, child, current, parentCheck=False):
    if current is None:
        return False

    if not parentCheck:
        if current.value == child.value:
            return False

        if current.value > parent.value:
            current = current.left
        elif current.value < parent.value:
            current = current.right

        else:
            # found node two from one or three
            parentCheck = True

    elif parentCheck:
        if current.value > child.value:
            current = current.left
        elif current.value < child.value:
            current = current.right
        else:
            # found third node after finding second in proper order
            return True

    return validateThreeNodesHelper(grandparent, parent, child, current, parentCheck)
