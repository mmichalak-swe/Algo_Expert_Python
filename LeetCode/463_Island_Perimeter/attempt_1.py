# O(N) time | O(1) space
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(row, col):
            if not 0 <= row < ROWS or not 0 <= col < COLS or grid[row][col] == 0:
                return 1
            elif grid[row][col] == 2:
                return 0
            
            grid[row][col] = 2
            
            return dfs(row - 1, col) + dfs(row, col + 1) + dfs(row + 1, col) + dfs(row, col - 1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return dfs(row, col)
