# O(n) time | O(1) space, where n is the length of the input array
# lines 9-10, because check on line 6 validates that min peak length is 3,
# add 3 on line 11 to the valid points from lines 9-10.
def longestPeak(array):
    maxPeak = 0
    i = 1
    while i < len(array) - 1:
        if array[i] <= array[i-1] or array[i] <= array[i+1]:
            i += 1 # skip value after not finding a peak
            continue
        leftValid = calcLeft(array, i - 1, i - 2)
        rightValid = calcRight(array, i + 1, i + 2)
        currPeak = leftValid + 3 + rightValid
        maxPeak = max(currPeak, maxPeak)
        i += rightValid + 2 # skip past found current peak to next candidate
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
