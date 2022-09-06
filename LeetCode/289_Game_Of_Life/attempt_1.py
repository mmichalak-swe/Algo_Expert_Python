DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

# O(n) time | O(1) space
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                neighborSum = 0
                
                for direction in DIRECTIONS:
                    newRow = row + direction[0]
                    newCol = col + direction[1]
                    
                    if not (0 <= newRow < ROWS) or not (0 <= newCol < COLS) or board[newRow][newCol] == '1':
                        continue
                    
                    neighborSum += abs(board[newRow][newCol])
                    
                if neighborSum == 3 and board[row][col] == 0: # dead cell becomes live
                    board[row][col] = '1'
                elif neighborSum <= 1: # dies due to underpop
                    board[row][col] *= -1
                elif 2 <= neighborSum <= 3: # lives on if alive
                    continue
                elif neighborSum > 3: # dies due to overpop
                    board[row][col] *= -1
                    
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == '1':
                    board[row][col] = 1
