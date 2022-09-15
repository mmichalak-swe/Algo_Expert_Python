<<<<<<< HEAD
# O(nm * min(n, m)) time | O(min(n, m)) space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return []
        small_list = list(text1) if len(text1) < len(text2) else list(text2)
        large_list = list(text2) if len(text2) > len(text1) else list(text1)

        board = [[None for _ in range(len(small_list) + 1)] for _ in range(2)]
        
        for i in range(1, len(large_list) + 1):
            large_ptr = i - 1
            for j in range(1, len(small_list) + 1):
                small_ptr = j - 1

                if small_list[small_ptr] == large_list[large_ptr]:
                    if board[0][j-1]:
                        board[1][j] = board[0][j-1][:]
                        board[1][j].append(small_list[small_ptr])
                    else:
                        board[1][j] = [small_list[small_ptr]]
                    continue

                oneUp = len(board[0][j]) if board[0][j] is not None else 0
                oneLeft = len(board[1][j-1]) if board[1][j-1] is not None else 0

                board[1][j] = board[1][j-1] if oneLeft >= oneUp else board[0][j]   

            board[0] = board[1][:]

        return len(board[-1][-1]) if board[-1][-1] else 0
=======
# First Solution: O(nm * min(n,m)) time | O(nm) space
# Second Solution: O(nm * min(n, m)) time | O(min(n, m)) space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return ""
        
        small = text1 if len(text1) < len(text2) else text2
        large = text2 if small == text1 else text1
        
#         board = [[0 for _ in range(len(small) + 1)] for _ in range(len(large) + 1)]
        
#         for i in range(1, len(large) + 1):
#             largePtr = i - 1
#             for j in range(1, len(small) + 1):
#                 smallPtr = j - 1
                
#                 if small[smallPtr] == large[largePtr]:
#                     if board[i-1][j-1]:
#                         board[i][j] = board[i-1][j-1] + 1
#                     else:
#                         board[i][j] = 1
#                     continue
                
#                 oneUp = board[i-1][j]
#                 oneLeft = board[i][j-1]
                
#                 board[i][j] = oneLeft if oneLeft >= oneUp else oneUp
        
#         # print(board)
#         return board[-1][-1]

        board = [[0 for _ in range(len(small) + 1)] for _ in range(2)]
    
        for i in range(1, len(large) + 1):
            largePtr = i - 1
            for j in range(1, len(small) + 1):
                smallPtr = j - 1
                
                if small[smallPtr] == large[largePtr]:
                    if board[0][j-1]:
                        board[1][j] = board[0][j-1] + 1
                    else:
                        board[1][j] = 1
                    continue
                
                oneUp = board[0][j]
                oneLeft = board[1][j-1]
                
                board[1][j] = oneLeft if oneLeft >= oneUp else oneUp
                
            board[0] = board[1][:]
        
        print(board)
        return board[-1][-1]
>>>>>>> 014d2ee63d3d929610c75092de629dc5c6e686b5
