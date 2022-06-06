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
            getValidSearch(nodesToSearch, matrix, row, col)
            while len(nodesToSearch) > 0:
                currNode = nodesToSearch.pop(0)
                new_x = currNode[0]
                new_y = currNode[1]
                if matrix[new_x][new_y] == 1 and (new_x, new_y) not in alreadyVisited:
                    getValidSearch(nodesToSearch, matrix, new_x, new_y, currNode[2])
                    alreadyVisited.append((new_x, new_y))
                    size += 1
                else:
                    continue
            riverSizes.append(size)

    return riverSizes


def getValidSearch(nodesToSearch, matrix, row, col, fromDirection=2):
    for i in range(4): # number/length of DIRECTIONS
        if i != fromDirection:
            row += DIRECTIONS[i][0]
            col += DIRECTIONS[i][1]
            if not (0 <= row < len(matrix)) or not (0 <= col < len(matrix[0])):
                row -= DIRECTIONS[i][0]
                col -= DIRECTIONS[i][1]
                continue
            else:
                nodesToSearch.append((row, col, (i+2)%4))
                row -= DIRECTIONS[i][0]
                col -= DIRECTIONS[i][1]
        else:
            continue
