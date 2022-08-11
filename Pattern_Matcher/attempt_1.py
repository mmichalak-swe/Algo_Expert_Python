# O(n^2 + m) time | O(n + m) space, where n is the length of the input string, and m
# is the length of the input pattern
def patternMatcher(pattern, string):
    swap = False

    # O(m) time and space
    if pattern[0] == 'y':
        swap =  True
        pattern = getNewPattern(pattern)
    else:
        pattern = [char for char in pattern]

    # O(n) time
    for lenOfX in range(1, len(string)):
        counts, firstYPos = getCountsAndFirstYPos(pattern, len(string), lenOfX)

        potentialX = string[:lenOfX]
        if 'y' in counts:
            lenOfY = (len(string) - (lenOfX * counts['x'])) // counts['y']
            potentialY = string[firstYPos:firstYPos + lenOfY]
        else:
            potentialY = ''

        # O(n) time and space
        potentialList = []
        for char in pattern:
            if char == 'x':
                potentialList.append(potentialX)
            else:
                potentialList.append(potentialY)

        # O(n) time and space
        potentialString = ''.join(potentialList)

        if potentialString == string:
            return [potentialX, potentialY] if swap == False else [potentialY, potentialX]

    return []


def getNewPattern(pattern):
    patternList = [char for char in pattern]
    for i in range(len(patternList)):
        patternList[i] = 'x' if patternList[i] == 'y' else 'y'
    return ''.join(patternList)


def getCountsAndFirstYPos(pattern, lenOfString, lenOfX):
    counts = {}
    # O(m) time
    for char in pattern:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    firstYInPattern = 0
    for char in pattern:
        if char == 'y':
            break
        firstYInPattern += 1
    firstYPos = lenOfX * firstYInPattern

    return counts, firstYPos
