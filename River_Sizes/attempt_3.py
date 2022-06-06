from collections import deque

#             SOUTH   EAST    NORTH    WEST
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def riverSizes(matrix):

    riverSizes = []
    alreadyVisited = [[False for value in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            value = matrix[row][col]

            if alreadyVisited[row][col] or value == 0:
                continue

            alreadyVisited[row][col] = True
            
            size = 1
            nodesToSearch = deque()
            getValidSearch(nodesToSearch, matrix, row, col, alreadyVisited)
            while len(nodesToSearch) > 0:
                currNode = nodesToSearch.popleft()
                new_x = currNode[0]
                new_y = currNode[1]
                if matrix[new_x][new_y] == 1 and not alreadyVisited[new_x][new_y]:
                    getValidSearch(nodesToSearch, matrix, new_x, new_y, alreadyVisited)
                    alreadyVisited[new_x][new_y] = True
                    size += 1
                else:
                    continue
            riverSizes.append(size)

    return riverSizes


def getValidSearch(nodesToSearch, matrix, row, col, alreadyVisited):
    for direction in DIRECTIONS: # number/length of DIRECTIONS
        new_row , new_col = row + direction[0], col + direction[1]
        if not (0 <= new_row < len(matrix)) or not (0 <= new_col < len(matrix[0])):
            continue
        else:
            if alreadyVisited[new_row][new_col]:
                continue
            else:
                nodesToSearch.append((new_row, new_col))
