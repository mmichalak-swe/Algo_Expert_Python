from collections import deque

# O(n*m) time | O(1) space
class Solution:
    shortestPath = float('inf')
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        d = deque()
        d.append((entrance[0], entrance[1], 0))
        
        while d:
            row, col, steps = d.popleft()
            
            if not 0 <= row < ROWS or not 0 <= col < COLS or maze[row][col] != '.':
                continue
            
            if (row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1) and steps > 0:
                    return steps

            d.append((row, col + 1, steps + 1))
            d.append((row + 1, col, steps + 1))
            d.append((row, col - 1, steps + 1))
            d.append((row - 1, col, steps + 1))
            
            maze[row][col] = '+'
        
        return -1
