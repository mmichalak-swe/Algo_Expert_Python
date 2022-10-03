# O(N) time | O(1) space, where N is n*n elements
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Transpose, rows become columns
        
        for row in range(ROWS):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Mirror 180, using middle col as axis. Can just reverse each row using [::-1]
        
        left = 0
        right = len(matrix[0]) - 1
        
        while left < right:
            for row in range(ROWS):
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
            left += 1
            right -= 1
