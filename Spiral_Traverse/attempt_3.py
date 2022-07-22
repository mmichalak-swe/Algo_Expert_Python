# O(n) time | O(n) space, where n is the # of values in the array
def spiralTraverse(array):
    startRow = 0
    endRow = len(array) - 1
    startCol = 0
    endCol = len(array[0]) - 1

    spiral = []
    
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            spiral.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            spiral.append(array[row][endCol])

        for col in range(endCol - 1, startCol - 1, -1):
            if startRow == endRow:
                break
            spiral.append(array[endRow][col])

        for row in range(endRow - 1, startRow, -1):
            if startCol == endCol:
                break
            spiral.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return spiral
