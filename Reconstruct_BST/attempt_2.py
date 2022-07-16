# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Index:
    def __init__(self, index):
        self.index = index

# O(n) time | O(n) space, where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    tracker = Index(0)
    return reconstructBstHelper(preOrderTraversalValues, float('-inf'), float('inf'), tracker)


def reconstructBstHelper(values, lowerBound, upperBound, tracker, currNode=None):
    if tracker.index >= len(values) or values[tracker.index] < lowerBound or values[tracker.index] >= upperBound:
        return

    currNode = BST(values[tracker.index])
    tracker.index += 1
    currNode.left = reconstructBstHelper(values, lowerBound, currNode.value, tracker, currNode.left)
    currNode.right = reconstructBstHelper(values, currNode.value, upperBound, tracker, currNode.right)
    
    return currNode
