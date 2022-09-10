# Both Solutions: O(N) time | O(1) space, where N is n*n elements
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        
#         # Mirror 180, using middle col as axis
        
#         left = 0
#         right = len(matrix[0]) - 1
        
#         while left < right:
#             for row in range(ROWS):
#                 matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
#             left += 1
#             right -= 1
        
#         # Mirror over diagonal from top right to bottom left
#         # not including those cells on the diagonal axis

#         for row in range(ROWS - 1):
#             for col in range(COLS - 1 - row):
#                 newRow = COLS - 1 - col
#                 newCol = ROWS - 1 - row
#                 matrix[row][col], matrix[newRow][newCol] = matrix[newRow][newCol], matrix[row][col]

                
        # Mirror 180, using horizonal middle as axis
        
        top = 0
        bottom = len(matrix) - 1
        
        while top < bottom:
            for row in range(ROWS):
                matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1
            
        print(matrix)
        
        # Transpose, rows become columns
        
        for row in range(ROWS):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
