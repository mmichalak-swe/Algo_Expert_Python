# O(n^2) time | O(d) space, where n is the num of nodes in each input array, respectively
# d is the depth (or height) of the BST that is represented
def sameBsts(arrayOne, arrayTwo):
    return sameBstHelper(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def sameBstHelper(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo

    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rightRootIdxOne = getIdxOfFirstLarger(arrayOne, rootIdxOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstLarger(arrayTwo, rootIdxTwo, maxVal)

    currentValue = arrayOne[rootIdxOne]
    left = sameBstHelper(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
    right = sameBstHelper(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)

    return left and right


def getIdxOfFirstSmaller(array, startIdx, minVal):
    for i in range(startIdx + 1, len(array)):
        if array[i] < array[startIdx] and array[i] >= minVal:
            return i
    return -1


def getIdxOfFirstLarger(array, startIdx, maxVal):
    for i in range(startIdx + 1, len(array)):
        if array[i] >= array[startIdx] and array[i] < maxVal:
            return i
    return -1
