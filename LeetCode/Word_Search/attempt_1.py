DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]



def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

    
    def dfs(row, col, searchIdx):
        if searchIdx == len(word):
            return True
        if not 0 <= row < ROWS or not 0 <= col < COLS or visited[row][col] or board[row][col] != word[searchIdx]:
            return False

        visited[row][col] = True
        
        for direction in DIRECTIONS:
            if dfs(row + direction[0], col + direction[1], searchIdx + 1):
                return True
            
        visited[row][col] = False


    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == word[0]:
                if dfs(row, col, 0):
                    return True
            else:
                continue

    return False
