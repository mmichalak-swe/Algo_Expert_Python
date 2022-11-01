# O(n * m) time | O(1) space
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        r, c = 0, COLS - 1
        
        while r < ROWS and 0 <= c < COLS:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        
        return False
