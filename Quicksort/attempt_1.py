# TIME:
# Best: O(n*log(n)), Average: O(n*log(n)), Worst: O(n^2)
# SPACE:
# Best/Average: O(log(n)), Worst: O(n)
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    # print(startIdx, endIdx)
    if startIdx >= endIdx:
        return

    # print(array[startIdx:endIdx + 1], startIdx, endIdx)

    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx

    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(array, leftIdx, rightIdx)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1

    swap(array, pivotIdx, rightIdx)
    # print(array)
    rightSideSmaller = rightIdx - 1 - startIdx > endIdx - (rightIdx) + 1

    if rightSideSmaller:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)
    else:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
