# O(N) time | O(1) space
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            if not 0 <= row < ROWS or not 0 <= col < COLS or board[row][col] != 'O':
                return
            
            # any spaces that touch border/remain O's, change temporarily to lowercase 'o'
            board[row][col] = 'o'
            
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
        
        # iterate through first row, last row, all columns
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        
        # iterate through col 0, last col, excluding row 0, last row
        for row in range(1, ROWS - 1):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'o':
                    board[row][col] = 'O'
        
        return board
