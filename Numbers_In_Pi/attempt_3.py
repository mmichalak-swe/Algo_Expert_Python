# O(n^3 + m) time | O(n + m) space, where n is the length of pi string
# n^3 = slicing input string (n), then double for-loop for each slice (n^2)
def numbersInPi(pi, numbers):
    table = {number:True for number in numbers} # O(m) operation, m = len(numbers)
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, numbers, cache, i)
    return -1 if cache[0] == float('inf') else cache[0]


def getMinSpaces(pi, table, cache, startIdx=0):
    if startIdx == len(pi):
        return -1
    if startIdx in cache:
        return cache[startIdx]
    minSpaces = float('inf')
    for i in range(startIdx, len(pi)):
        current = pi[startIdx : i+1] # adds factor of 'n' to time complexity
        if current in table:
            minSpacesLeft = getMinSpaces(pi, table, cache, i+1)
            minSpaces = min(minSpaces, minSpacesLeft + 1)
    cache[startIdx] = minSpaces
    return cache[startIdx]
