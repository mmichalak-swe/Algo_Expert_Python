# BEST/AVERAGE: O(n) time | O(1) space
# WORST: O(n^2) time | O(1) space
def quickselect(array, k):
    kthPosition = k - 1
    return quickSelectHelper(array, 0, len(array) - 1, kthPosition)


def quickSelectHelper(array, startIdx, endIdx, kthPosition):
    while True:
        if startIdx > endIdx:
            raise Exception("Something is wrong!")

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

        if rightIdx == kthPosition:
            return array[rightIdx]
        elif rightIdx < kthPosition:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1

def swap(array, idxOne, idxTwo):
    array[idxOne], array[idxTwo] = array[idxTwo], array[idxOne]
