# DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# O(N) time | O(1) space
# Commented solution is BFS, uncommented is DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         output = 0
        
#         for row in range(len(grid)):
#             for col in range(len(grid[row])):
#                 if grid[row][col] == '1':
#                     output += 1
#                     stack = [(row, col)]
#                     while stack:
#                         newRow, newCol = stack.pop()
#                         grid[newRow][newCol] = '2'
#                         for direction in DIRECTIONS:
#                             potentialRow = newRow + direction[0]
#                             potentialCol = newCol + direction[1]
#                             if not (0 <= potentialRow < len(grid)) or not (0 <= potentialCol < len(grid[0])):
#                                 continue
#                             if grid[potentialRow][potentialCol] == '1':
#                                 stack.append((potentialRow, potentialCol))
#                 else:
#                     continue
                    
#         return output

        ROWS, COLS = len(grid), len(grid[0])
    
        def dfs(row, col):
            if not 0 <= row < ROWS or not 0 <= col < COLS or grid[row][col] != '1':
                return
            
            grid[row][col] = '0'
            
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
        
        numIslands = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    dfs(row, col)
                    numIslands += 1
        
        return numIslands
