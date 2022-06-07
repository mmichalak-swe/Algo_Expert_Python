from collections import deque
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def removeIslands(matrix):
    if len(matrix) < 3 or len(matrix[0]) < 3:
        return matrix
    
    nodesToExclude = [[False for col in matrix[0]] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (1 <= row < len(matrix) - 1) and (1 <= col < len(matrix[0]) - 1):
                continue
            if matrix[row][col] == 1:
                findAttached(matrix, row, col, nodesToExclude)
            else:
                continue

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[0]) - 1):
            if matrix[row][col] == 1 and not nodesToExclude[row][col]:
                matrix[row][col] = 0

    return matrix


def findAttached(matrix, row, col, nodesToExclude):
    nodesToExplore = deque()
    nodesToExplore.append((row, col))
    while len(nodesToExplore) > 0:
        node = nodesToExplore.popleft()
        for i in range(4):
            new_row = node[0] + DIRECTIONS[i][0]
            new_col = node[1] + DIRECTIONS[i][1]
            if not (0 <= new_row < len(matrix)) or not (0 <= new_col < len(matrix[0])):
                continue
            if matrix[new_row][new_col] == 1 and not nodesToExclude[new_row][new_col]:
                nodesToExclude[new_row][new_col] = True
                nodesToExplore.append((new_row, new_col))
            else:
                continue
