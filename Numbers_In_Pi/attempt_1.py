# O(n^3 + m) time | O(n) space, where n is the length of pi string
# n^3 = slicing input string (n), then double for-loop for each slice (n^2)
# DOESN'T PASS ALL TEST CASES
def numbersInPi(pi, numbers):
    table = {number:True for number in numbers}
    spaces = float('inf')

    for i in range(len(pi) + 1):
        current = pi[:i]
        if current in table:
            output = recursiveHelper(pi, table, i)
            if output == 0:
                output = None
            if output is not None and output < spaces:
                spaces = output

    return spaces if spaces != float('inf') else -1


def recursiveHelper(pi, table, startIdx=0, spaces=0):
    for i in range(startIdx, len(pi) + 1):
        current = pi[startIdx:i+1]
        if current in table:
            check = recursiveHelper(pi, table, i+1, spaces+1)
            if check:
                return check

    return spaces
