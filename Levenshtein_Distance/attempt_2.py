# O(nm) time | O(min(len(n), len(m))) space - where n and m are the lengths of str 1,
# str 2, if len(str1) < len(str2). Attempt 3 fixes this constraint
def levenshteinDistance(str1, str2):
    board = [[c for c in range(len(str2) + 1)] for r in range(2)]

    for r in range(1, len(str1) + 1):
        for c in range(len(str2) + 1):
            if c == 0:
                board[1][0] = board[0][0] + 1
            elif str1[r-1] == str2[c-1]:
                board[1][c] = board[0][c-1]
            else:
                board[1][c] = 1 + min(board[0][c], board[0][c-1], board[1][c-1])
        board[0] = board[1][:]

    return board[1][len(str2)]
