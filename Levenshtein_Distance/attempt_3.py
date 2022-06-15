# O(rc) time | O(min(len(str1), len(str2))) space
def levenshteinDistance(str1, str2):
    small = None
    large = None
    len_small = 0
    len_large = 0

    if len(str1) < len(str2):
        small = str1
        large = str2
        len_small = len(str1)
        len_large = len(str2)
    else:
        small = str2
        large = str1
        len_small = len(str2)
        len_large = len(str1)

    board = [[c for c in range(len_large + 1)] for r in range(2)]

    for r in range(1, len_small + 1):
        for c in range(len_large + 1):
            if c == 0:
                board[1][0] = board[0][0] + 1
            elif small[r-1] == large[c-1]:
                board[1][c] = board[0][c-1]
            else:
                board[1][c] = 1 + min(board[0][c], board[0][c-1], board[1][c-1])
        board[0] = board[1][:]

    return board[1][len_large]

x = "table"
y = "bal"

print(levenshteinDistance(x, y))