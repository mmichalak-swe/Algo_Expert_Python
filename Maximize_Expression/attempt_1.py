# Brute force approach
# O(n^4) time | O(1) space, where n is the length of the input array
def maximizeExpression(array):
    maxExp = float('-inf')
    
    for a in range(len(array)):
        aVal = array[a]
        for b in range(a+1, len(array)):
            bVal = array[b]
            for c in range(b+1, len(array)):
                cVal = array[c]
                for d in range(c+1, len(array)):
                    dVal = array[d]

                    potentialMax = evaluateExp(aVal, bVal, cVal, dVal)
                    maxExp = max(maxExp, potentialMax)

    if maxExp == float('-inf'):
        return 0
    else:
        return maxExp


def evaluateExp(a, b, c, d):
    return a - b + c - d
