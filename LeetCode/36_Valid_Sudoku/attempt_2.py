# O(1) time | O(1) space, where N is the total number of values in the board (81)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # function to validate rows, cols, sub-boxes
        def isValid(items):
            values = [item for item in items if item != '.']
            return len(set(values)) == len(values)
        
        # validate rows
        for row in board:
            if not isValid(row):
                return False
        
        # validate cols
        for col in zip(*board):
            if not isValid(col):
                return False
        
        # validate sub-boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                subBox = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
                        
                if not isValid(subBox):
                    return False

        return True
