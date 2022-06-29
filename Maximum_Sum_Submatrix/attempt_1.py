# Brute force approach
# O(w*h*size^2) time | O(1) space, where w is the width of the matrix, h is the height
def maximumSumSubmatrix(matrix, size):
    maxSum = float('-inf')

    for row in range(len(matrix) - size + 1):
        for col in range(len(matrix[row]) - size + 1):
            tempSum = 0
            for i in range(size):
                for j in range(size):
                    tempSum += matrix[row+i][col+j]
            if tempSum > maxSum:
                maxSum = tempSum

    return maxSum
