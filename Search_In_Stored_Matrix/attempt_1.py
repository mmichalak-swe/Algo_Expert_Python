def searchInSortedMatrix(matrix, target):
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row]) - 1, -1, -1):
            num = matrix[row][col]
            if num > target:
                continue
            elif num < target:
                break
            else:
                return [row, col]

    return [-1, -1]
