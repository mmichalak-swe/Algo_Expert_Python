DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def orangesRotting(grid):
    numRows = len(grid)
    if numRows == 0:
        return -1
    numCols = len(grid[0])
    stackEven = []
    stackOdd = []

    numFresh = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 2:
                stackEven.append([row, col])
            elif grid[row][col] == 1:
                numFresh += 1

    minute = 0
    while numFresh != 0 and (stackEven or stackOdd):
        if minute % 2 == 0:
            while stackEven:
                rottenOrange = stackEven.pop()
                rottenRow = rottenOrange[0]
                rottenCol = rottenOrange[1]

                for direction in DIRECTIONS:
                    newRow = rottenRow + direction[0]
                    newCol = rottenCol + direction[1]

                    if isValid(newRow, newCol, numRows, numCols) and grid[newRow][newCol] == 1:
                        stackOdd.append([newRow, newCol])
                        grid[newRow][newCol] = 2
                        numFresh -= 1

        elif minute % 2 != 0:
            while stackOdd:
                rottenOrange = stackOdd.pop()
                rottenRow = rottenOrange[0]
                rottenCol = rottenOrange[1]

                for direction in DIRECTIONS:
                    newRow = rottenRow + direction[0]
                    newCol = rottenCol + direction[1]

                    if isValid(newRow, newCol, numRows, numCols) and grid[newRow][newCol] == 1:
                        stackEven.append([newRow, newCol])
                        grid[newRow][newCol] = 2
                        numFresh -= 1

        minute += 1

    return minute if numFresh == 0 else -1


def isValid(row, col, numRows, numCols):
    return 0 <= row < numRows and 0 <= col < numCols
