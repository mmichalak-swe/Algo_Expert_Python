# Non-optimal, uses array instead of heap (heap is more optimal)
# O(v^2 + e) time | O(v) space, where v is the number of vertices, and e is the number
# of edges in the input graph
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
    minDistances = [float('inf') for edge in range(numberOfVertices)]
    minDistances[start] = 0

    visited = set()

    while len(visited) != numberOfVertices:
        vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)

        if currentMinDistance == float('inf'):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance

    # return list(map(lambda x: -1 if x == float('inf') else x, minDistances))
    minDistances = [x if x != float('inf') else -1 for x in minDistances]
    return minDistances


def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float('inf')
    vertex = None

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance

    return vertex, currentMinDistance
