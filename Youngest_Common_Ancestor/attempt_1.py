# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# O(d) time | O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    descendantOneDepth = getNodeDepth(topAncestor, descendantOne)
    descendantTwoDepth = getNodeDepth(topAncestor, descendantTwo)

    deeperNode = descendantOne if descendantOneDepth >= descendantTwoDepth else descendantTwo
    shallowerNode = descendantTwo if descendantTwoDepth <= descendantOneDepth else descendantOne

    differenceInDepths = abs(descendantOneDepth - descendantTwoDepth)
    for i in range(differenceInDepths):
        deeperNode = deeperNode.ancestor

    while deeperNode.name != shallowerNode.name:
        deeperNode = deeperNode.ancestor
        shallowerNode = shallowerNode.ancestor

    return deeperNode


def getNodeDepth(topAncestor, descendant):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth
