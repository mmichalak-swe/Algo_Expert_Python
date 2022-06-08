# O(n^2) time | O(n) space, where n is the length of the edges list
# or, n = the number of vertices
def cycleInGraph(edges):
    length_Edges = len(edges)
    for i in range(length_Edges):
        if recursiveCycle(edges, i, length_Edges):
            return True
    return False


def recursiveCycle(edges, startIdx, length_Edges, count=0, currIdx=None):
    if count > length_Edges:
        return

    if currIdx == startIdx:
        return True

    if currIdx is None:
        currIdx = startIdx

    for toIdx in edges[currIdx]:
        check = recursiveCycle(edges, startIdx, length_Edges, count+1, toIdx)
        if check:
            return True
