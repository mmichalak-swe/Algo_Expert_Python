# O(3N) time | O(1) space, where N is the total number of values in the board (81)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        # validate rows
        for row in range(ROWS):
            table = {x: False for x in "123456789"}
            
            for col in range(COLS):
                num = board[row][col]
                
                if num == '.':
                    continue
                if table[num] is True:
                    return False
                else:
                    table[num] = True
        
        # validate cols
        for col in range(COLS):
            table = {x: False for x in "123456789"}
            
            for row in range(ROWS):
                num = board[row][col]

                if num == '.':
                    continue
                if table[num] is True:
                    return False
                else:
                    table[num] = True
        
        # validate sub-boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                table = {x: False for x in "123456789"}

                for rowOffset in range(3):
                    for colOffset in range(3):
                        num = board[row + rowOffset][col + colOffset]
                        
                        if num == '.':
                            continue
                        if table[num] is True:
                            return False
                        else:
                            table[num] = True
        
        return True
