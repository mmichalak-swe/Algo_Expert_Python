# O(n) time | O(1) space, where n is the length of the input array
def longestPeak(array):
    maxPeak = 0
    for i in range(1, len(array) - 1):
        leftPeaks = calcLeft(array, i, i - 1)
        rightPeaks = calcRight(array, i, i + 1)
        if leftPeaks == 0 or rightPeaks == 0:
            continue
        currPeak = leftPeaks + 1 + rightPeaks
        maxPeak = max(currPeak, maxPeak)
    return maxPeak


def calcLeft(array, currIdx, leftIdx):
    validLeftNodes = 0
    while leftIdx >= 0:
        if array[leftIdx] < array[currIdx]:
            validLeftNodes += 1
        else:
            break
        currIdx -= 1
        leftIdx -= 1
    return validLeftNodes


def calcRight(array, currIdx, rightIdx):
    validRightNodes = 0
    while rightIdx < len(array):
        if array[rightIdx] < array[currIdx]:
            validRightNodes += 1
        else:
            break
        currIdx += 1
        rightIdx += 1
    return validRightNodes
