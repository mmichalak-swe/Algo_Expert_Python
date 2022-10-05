# O(1) time | O(n) space
# added scalability option with n variable for larger boards
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['' for _ in range(3)] for _ in range(3)]
        
        player1 = True
        n = 3

        for move in moves:
            if player1:
                board[move[0]][move[1]] = 'X'
            else:
                board[move[0]][move[1]] = 'O'
            
            player1 = not player1
        
        for row in board:
            result = ''.join(row)
            if result == 'X' * n:
                return "A"
            elif result == 'O' * n:
                return "B"
        
        for col in range(n):
            result = ''
            for row in range(n):
                result += board[row][col]
            if result == 'X' * n:
                return "A"
            elif result == 'O' * n:
                return "B"
        
        result = ''
        for idx in range(n):
            result += board[idx][idx]
        
        if result == 'X' * n:
            return "A"
        elif result == 'O' * n:
            return "B"
        
        result = ''
        col = n - 1
        for row in range(n):
            result += board[row][col]
            col -= 1
        
        if result == 'X' * n:
            return "A"
        elif result == 'O' * n:
            return "B"
        
        if len(moves) == (n * n):
            return "Draw"
        else:
            return "Pending"
