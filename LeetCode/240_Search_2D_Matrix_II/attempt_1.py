# O(ROWS * log(m)) time | O(1) space
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for targetRow in range(ROWS):
            if matrix[targetRow][0] > target:
                break

            left = 0
            right = COLS - 1
        
            while left <= right:
                mid = (left + right) // 2

                val = matrix[targetRow][mid]

                if val < target:
                    left = mid + 1
                elif val > target:
                    right = mid - 1
                else:
                    return True
        
        return False
