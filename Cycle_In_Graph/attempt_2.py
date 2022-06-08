from collections import deque

# O(v + e) time | O(v) space, where n is the length of the edges list
# or, n = the number of vertices
def cycleInGraph(edges):
    dfsState = [0] * len(edges)
    for i in range(len(edges)):
        if recursiveCycle(edges, i, dfsState):
            return True
    return False


# 0 = not visited yet
# 1 = currently in the recursize call stack
# 2 = already visited, doesn't yield a cycle
def recursiveCycle(edges, startIdx, dfsState):
    if dfsState[startIdx] == 0:
        dfsState[startIdx] = 1
    elif dfsState[startIdx] == 1:
        return True
    elif dfsState[startIdx] == 2:
        return

    for num in edges[startIdx]:
        check = recursiveCycle(edges, num, dfsState)
        if check:
            return True

    dfsState[startIdx] = 2
