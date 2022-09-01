DIRECTIONS = [(-1, 1), (-1, 0), (-1, -1)]

class Solution:
    # First Solution: O(n) time | O(n) space, where n is the number of elements in the input matrix
    # Second Solution: O(n) time | O(1) space, where n is the number of elements in the input matrix
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         ROWS, COLS = len(matrix), len(matrix[0])
        
#         if ROWS == 1:
#             return matrix[0][0]
        
#         minValue = float('inf')

#         visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
#         currRow = [matrix[-1][col] for col in range(COLS)]
#         nextRow = currRow[:]

#         for row in range(ROWS - 1, 0, -1): # from second to last row, to 0
#             for col in range(COLS - 1, -1, -1): # all cols, from greatest to least
#                 for direction in DIRECTIONS:
#                     newRow = row - 1
#                     newCol = col + direction[1]

#                     if not (0 <= newCol < COLS): # newRow will always be valid because of row range
#                         continue

#                     if not visited[newRow][newCol]:
#                         nextRow[newCol] = currRow[col] + matrix[newRow][newCol]
#                         visited[newRow][newCol] = True
#                     else:
#                         nextRow[newCol] = min(nextRow[newCol], currRow[col] + matrix[newRow][newCol])

#                     if row == 1:
#                         minValue = min(minValue, nextRow[newCol])

#             currRow = nextRow[:]

#         return minValue


        ROWS, COLS = len(matrix), len(matrix[0])
        
        if ROWS == 1:
            return matrix[0][0]
        
        minValue = float('inf')
        
        for row in range(1, ROWS):
            for col in range(COLS):
                if col == 0:
                    matrix[row][col] = min(matrix[row - 1][col], matrix[row - 1][col + 1]) + matrix[row][col]
                elif col == COLS - 1:
                    matrix[row][col] = min(matrix[row - 1][col], matrix[row - 1][col - 1]) + matrix[row][col]
                else:
                    matrix[row][col] = min(matrix[row - 1][col - 1], matrix[row - 1][col], matrix[row - 1][col + 1]) + matrix[row][col]
                if row == ROWS - 1:
                    minValue = min(minValue, matrix[row][col])
        
        return minValue
