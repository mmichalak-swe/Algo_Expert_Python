# Second Solution: O(log(n)) time | O(1) space "Virtual Flatten"
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix),len(matrix[0])
        start = 0
        end = ROWS*COLS - 1

        while start <= end:

            mid = (start+end) // 2
            num = matrix[mid//COLS][mid%COLS]

            if num > target:
                end = mid - 1
            elif num < target:
                start = mid + 1
            else:
                return True

        return False
