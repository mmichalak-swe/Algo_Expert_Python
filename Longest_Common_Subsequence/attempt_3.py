# O(nm) time | O(nm) space, where n and m are the lengths of the input strings
def longestCommonSubsequence(str1, str2):
    lcs = [[[None, 0, None, None] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    for row in range(1, len(str2) + 1):
        for col in range(1, len(str1) + 1):
            if str2[row - 1] == str1[col - 1]:
                lcs[row][col] = [str2[row - 1], lcs[row - 1][col - 1][1] + 1, row - 1, col - 1]
            else:
                if lcs[row - 1][col][1] > lcs[row][col - 1][1]:
                    lcs[row][col] = [None, lcs[row - 1][col][1], row - 1, col]
                else:
                    lcs[row][col] = [None, lcs[row][col - 1][1], row, col - 1]
    return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []
    row = len(lcs) - 1
    col = len(lcs[0]) - 1
    while row != 0 and col != 0:
        current = lcs[row][col]
        if current[0] is not None:
            sequence.append(current[0])
        row = current[2]
        col = current[3]
    return list(reversed(sequence))
