DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def pacificAtlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pacific = [[False for _ in range(COLS)] for _ in range(ROWS)]
    atlantic = [[False for _ in range(COLS)] for _ in range(ROWS)]
    
    def dfs(row, col, visited, prevHeight):
        if row < 0 or row == ROWS or col < 0 or col == COLS or heights[row][col] < prevHeight or visited[row][col]:
            return
        currentHeight = heights[row][col]
        visited[row][col] = True
        for direction in DIRECTIONS:
            dfs(row + direction[0], col + direction[1], visited, currentHeight)
    
    for row in range(ROWS):
        for col in range(COLS):
            if row == 0 or col == 0 and not pacific[row][col]:
                dfs(row, col, pacific, heights[row][col])
            if row == len(heights) - 1 or col == len(heights[row]) - 1:
                dfs(row, col, atlantic, heights[row][col])
    
    output = []
    for row in range(ROWS):
        for col in range(COLS):
            if pacific[row][col] and atlantic[row][col]:
                output.append([row, col])
                
    return output
