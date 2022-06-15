# O(rc) time | O(rc) space
def levenshteinDistance(str1, str2):
    board = [[None for c in range(len(str2) + 1)] for r in range(len(str1) + 1)]

    for r in range(len(str1) + 1):
        for c in range(len(str2) + 1):
            if r == 0:
                board[r][c] = c
            elif c == 0:
                board[r][c] = r
            elif str1[r-1] == str2[c-1]:
                board[r][c] = board[r-1][c-1]
            else:
                board[r][c] = 1 + min(board[r-1][c], board[r-1][c-1], board[r][c-1])

    return board[len(str1)][len(str2)]
