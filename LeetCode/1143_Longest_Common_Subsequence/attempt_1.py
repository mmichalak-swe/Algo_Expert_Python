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
