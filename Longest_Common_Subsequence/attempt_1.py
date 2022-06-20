# O(nm * min(n, m)) time | O(nm * (n, m)) space,
# where n and m are the lengths of the input strings
def longestCommonSubsequence(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return []
    str1_list = list(str1)
    str2_list = list(str2)

    board = [[None for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    for i in range(1, len(board)):
        str2_ptr = i - 1
        for j in range(1, len(board[i])):
            str1_ptr = j - 1

            if str1[str1_ptr] == str2[str2_ptr]:
                if board[i-1][j-1]:
                    board[i][j] = board[i-1][j-1][:]
                    board[i][j].append(str1[str1_ptr])
                else:
                    board[i][j] = [str1[str1_ptr]]
                continue

            oneUp = len(board[i-1][j]) if board[i-1][j] is not None else 0
            oneLeft = len(board[i][j-1]) if board[i][j-1] is not None else 0

            board[i][j] = board[i][j-1] if oneLeft >= oneUp else board[i-1][j]    

    return board[-1][-1]
