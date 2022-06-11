# O(b*s) time | O(1) space, where b is len bigString, s is len smallString
# worst case, iterate through bigString fully, len(smallStrings) times

def multiStringSearch(bigString, smallStrings):
    output = [False for _ in smallStrings]
    for i, smallString in enumerate(smallStrings):
        bigIdx = 0

        while bigIdx != len(bigString):
            if bigString[bigIdx] == smallString[0]:
                if compareHelper(bigString, bigIdx, smallString):
                    output[i] = True
                    break
            bigIdx += 1

    return output


def compareHelper(bigString, bigIdx, smallString):
    for i in range(len(smallString)):
        if bigIdx >= len(bigString):
            return False
        if smallString[i] != bigString[bigIdx]:
            return False
        bigIdx += 1
    return True
