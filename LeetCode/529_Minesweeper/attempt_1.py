# O(N) time | O(1) space
# time complexity is len*width of board, times 9
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        ROWS, COLS = len(board), len(board[0])
        sweep = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        def isValidSpot(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def dfsHelper(row, col):
            if board[row][col] != 'E':
                return

            numMines = 0
            for spot in sweep:
                newRow, newCol = row + spot[0], col + spot[1]

                if isValidSpot(newRow, newCol) and board[newRow][newCol] == 'M':
                    numMines += 1

            if numMines == 0:
                board[row][col] = 'B'
            else:
                board[row][col] = str(numMines)
                return

            for spot in sweep:
                newRow, newCol = row + spot[0], col + spot[1]
                if isValidSpot(newRow, newCol):
                    dfsHelper(newRow, newCol)


        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        row = click[0]
        col = click[1]

        dfsHelper(row, col)

        return board
