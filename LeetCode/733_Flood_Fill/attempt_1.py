# O(N) time | O(1) space
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        
        def dfs(row, col, startColor=image[sr][sc]):
            if not 0 <= row < ROWS or not 0 <= col < COLS or image[row][col] != startColor:
                return
            
            image[row][col] = color
            
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)


        if image[sr][sc] != color:
            dfs(sr, sc)
        
        return image
