# Dynamic Programming Solution
# O(wh) time | O(wh) space, where w, h are width, height respectively
def numberOfWaysToTraverseGraph(width, height):
    graph = [[1 for h in range(1, height+1)] for w in range(width)]

    for row in range(1, width):
        for col in range(height):
            if col == 0:
                graph[row][0] = 1
            else:
                graph[row][col] = graph[row-1][col] + graph[row][col-1]

    return graph[-1][-1]
