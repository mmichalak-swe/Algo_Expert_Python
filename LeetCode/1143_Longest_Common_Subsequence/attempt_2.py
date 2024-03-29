# Second Solution: O(nm * min(n, m)) time | O(min(n, m)) space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return ""
        
        small = text1 if len(text1) < len(text2) else text2
        large = text2 if small == text1 else text1

        board = [[0 for _ in range(len(small) + 1)] for _ in range(2)]
    
        for i in range(1, len(large) + 1):
            largePtr = i - 1
            for j in range(1, len(small) + 1):
                smallPtr = j - 1
                
                if small[smallPtr] == large[largePtr]:
                    board[1][j] = board[0][j-1] + 1
                    continue
                
                oneUp = board[0][j]
                oneLeft = board[1][j-1]
                
                board[1][j] = oneLeft if oneLeft > oneUp else oneUp
                
            board[0] = board[1][:]

        return board[-1][-1]
