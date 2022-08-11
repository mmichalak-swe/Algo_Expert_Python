# O(n^2 + m) time | O(n + m) space, where n is the length of the input string, and m
# is the length of the input pattern
def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []

    # O(m) time and space
    newPattern, swapped = getNewPattern(pattern)
    counts, firstYPos = getCountsAndFirstYPos(newPattern, len(string))

    # O(n) time
    for lenOfX in range(1, len(string)):
        if 'y' in counts:  
            lenOfY = (len(string) - (lenOfX * counts['x'])) / counts['y']
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue
            lenOfY = int(lenOfY)
            yIdx = firstYPos * lenOfX
            potentialY = string[yIdx : yIdx + lenOfY]
        else:
            potentialY = ''

        potentialX = string[:lenOfX]
        
        # O(n) time and space
        potentialList = []
        for char in newPattern:
            if char == 'x':
                potentialList.append(potentialX)
            else:
                potentialList.append(potentialY)

        # O(n) time and space
        if string == ''.join(potentialList):
            return [potentialX, potentialY] if swapped == False else [potentialY, potentialX]

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
