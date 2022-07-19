# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(d) time | O(1) space, where d is the distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    return validateThreeNodesHelper(nodeOne, nodeTwo, nodeThree) or validateThreeNodesHelper(nodeThree, nodeTwo, nodeOne)


def validateThreeNodesHelper(current, parent, child):
    while current is not None and current is not parent:
        if current == child:
            return False
        current = current.left if parent.value < current.value else current.right

    while current is not None and current is not child:
        current = current.left if child.value < current.value else current.right

    return current == child
