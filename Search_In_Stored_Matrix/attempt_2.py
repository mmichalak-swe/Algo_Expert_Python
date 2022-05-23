# O(r + c) time | O(1) space
# where r is len of rows, c is len of cols

def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[row]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]

    return [-1, -1]
