#             SOUTH   EAST    NORTH    WEST
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# O(n*log(wh)) time | O(wh) space where n = # of spaces,
# w is width of matrix, h is height of matrix
def riverSizes(matrix):

    riverSizes = []
    alreadyVisited = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            value = matrix[row][col]

            if (row, col) in alreadyVisited or value == 0:
                continue

            alreadyVisited.append((row, col))
            
            size = 1
            nodesToSearch = []
            getValidSearch(nodesToSearch, matrix, row, col, alreadyVisited)
            while len(nodesToSearch) > 0:
                currNode = nodesToSearch.pop(0)
                new_x = currNode[0]
                new_y = currNode[1]
                if matrix[new_x][new_y] == 1 and (new_x, new_y) not in alreadyVisited:
                    getValidSearch(nodesToSearch, matrix, new_x, new_y, alreadyVisited)
                    alreadyVisited.append((new_x, new_y))
                    size += 1
                else:
                    continue
            riverSizes.append(size)

    return riverSizes


def getValidSearch(nodesToSearch, matrix, row, col, alreadyVisited):
    for i in range(4): # number/length of DIRECTIONS
        new_row = row + DIRECTIONS[i][0]
        new_col = col + DIRECTIONS[i][1]
        if (new_row, new_col) in alreadyVisited:
            continue
        else:
            if not (0 <= new_row < len(matrix)) or not (0 <= new_col < len(matrix[0])):
                continue
            else:
                nodesToSearch.append((new_row, new_col))
