from collections import deque
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# O(wh) time | O(wh) space where w, h are the width, height of the input matrix
def removeIslands(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if num_rows < 3 or len(matrix[0]) < 3:
        return matrix

    for row in range(num_rows):
        for col in range(num_cols):
            if (1 <= row < num_rows - 1) and (1 <= col < num_cols - 1):
                continue
            if matrix[row][col] == 1:
                findAttachedOnes(matrix, row, col, num_rows, num_cols)
            else:
                continue

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] > 0:
                matrix[row][col] -= 1

    return matrix


def findAttachedOnes(matrix, row, col, num_rows, num_cols):
    nodesToExplore = deque()
    nodesToExplore.append((row, col))
    while len(nodesToExplore) > 0:
        curr = nodesToExplore.popleft()
        currRow, currCol = curr[0], curr[1]
        for i in range(4):
            new_row = currRow + DIRECTIONS[i][0]
            new_col = currCol + DIRECTIONS[i][1]
            if not (0 <= new_row < num_rows) or not (0 <= new_col < num_cols):
                continue
            if matrix[new_row][new_col] == 1:
                nodesToExplore.append((new_row, new_col))
            else:
                continue
        matrix[currRow][currCol] = 2
