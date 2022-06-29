# Optimal approach
# O(w*h) time | O(w*h) space, where w is the width of the matrix, h is the height
def maximumSumSubmatrix(matrix, size):
    maxSum = float('-inf')
    sums = [[0 for _ in matrix[0]] for _ in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row == 0 and col == 0:
                sums[row][col] = matrix[row][col]
            elif row == 0:
                sums[row][col] = matrix[row][col] + sums[row][col-1]
            elif col == 0:
                sums[row][col] = matrix[row][col] + sums[row-1][col]
            else:
                sums[row][col] = matrix[row][col] + sums[row-1][col] + sums[row][col-1] - sums[row-1][col-1]

            temp = float('-inf')
            
            if row >= size - 1 and col >= size - 1:
                temp = sums[row][col]
            if col >= size:
                temp -= sums[row][col-size]
            if row >= size:
                temp -= sums[row-size][col]
            if row >= size and col >= size:
                temp += sums[row-size][col-size]

            maxSum = temp if temp > maxSum else maxSum

    return maxSum
