# O(N) time | O(1) space
# N = rows * cols
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        output = [-1 for ball in range(COLS)]
        
        for col in range(COLS):
            ball = col
            row = 0
            
            while row < ROWS:
                # if ball == 0 and grid[row][ball] == -1:
                #     break
                # if ball == (COLS - 1) and grid[row][ball] == 1:
                #     break

                slope = grid[row][ball]
                
                # if 0 and trying to move left, or at COLS - 1 and trying to move right
                if not 0 <= ball + slope < COLS:
                    break

                # if grid[row][ball] == 1 and grid[row][ball + 1] != 1:
                #     break
                # if grid[row][ball] == -1 and grid[row][ball - 1] != -1:
                #     break
                
                if grid[row][ball + slope] != slope:
                    break

                ball += slope
                row += 1
            
            if row == ROWS:
                output[col] = ball
        
        return output
