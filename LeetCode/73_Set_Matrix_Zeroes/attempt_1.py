class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        firstRowZero = False
        firstColZero = False
        
        zeroZero = True if matrix[0][0] == 0 else False
        
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row == 0:
                        firstRowZero = True
                    if col == 0:
                        firstColZero = True
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1, ROWS):
            for col in range(1, COLS):
                matrix[row][col] = 0 if matrix[row][0] == 0 or matrix[0][col] == 0 else matrix[row][col]

        if firstRowZero:
            for col in range(COLS):
                matrix[0][col] = 0

        if firstColZero:
            for row in range(ROWS):
                matrix[row][0] = 0
