# O(n^2 + m) time | O(n + m) space, where n is the length of the input string, and m
# is the length of the input pattern
def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []

    # O(m) time and space
    newPattern, swapped = getNewPattern(pattern)
    counts, firstYPos = getCountsAndFirstYPos(newPattern, len(string))

    # O(n) time
    if 'y' in counts:
        for lenOfX in range(1, len(string)):
            lenOfY = (len(string) - (lenOfX * counts['x'])) / counts['y']
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue
            lenOfY = int(lenOfY)
            yIdx = firstYPos * lenOfX
            potentialY = string[yIdx : yIdx + lenOfY]

            potentialX = string[:lenOfX]
            
            # O(n) time and space
            potentialList = map(lambda char: potentialX if char == 'x' else potentialY, newPattern)

            # O(n) time and space
            if string == ''.join(potentialList):
                return [potentialX, potentialY] if swapped == False else [potentialY, potentialX]

    else:
        lenOfX = len(string) / counts['x']
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            potentialX = string[:lenOfX]
            potentialList = map(lambda char: potentialX, newPattern)
            if string == ''.join(potentialList):
                return ['', potentialX] if swapped else [potentialX, '']
    return []


def getNewPattern(pattern):
    patternList = list(pattern)
    if pattern[0] == 'y':
        return list(map(lambda char: 'x' if char == 'y' else 'y', pattern)), True
    else:
        return patternList, False


def getCountsAndFirstYPos(pattern, lenOfString):
    counts = {}
    firstYInPattern = None
    # O(m) time
    for i, char in enumerate(pattern):
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            if char == 'y':
                firstYInPattern = i

    return counts, firstYInPattern
