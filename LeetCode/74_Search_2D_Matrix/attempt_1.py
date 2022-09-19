# First Solution: O(log(n)) time | O(1) space
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        
        while 0 <= row < ROWS and 0 <= col < COLS and matrix[row][col] >= target:
            if matrix[row][col] == target:
                return True
            if matrix[row][0] > target:
                row -= 1
            elif matrix[row][0] <= target:
                col -= 1

        return False
