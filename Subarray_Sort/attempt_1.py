# O(n) time | O(1) space, where n is the length of the input array
def subarraySort(array):
    smallestOutOfOrder = float('inf')
    largestOutOfOrder = float('-inf')

    indices = [-1, -1]

    for i in range(1, len(array)):
        smallIdx = i
        largeIdx = len(array) - 1 - i
        if array[smallIdx] < array[smallIdx-1]:
            smallestOutOfOrder = min(smallestOutOfOrder, array[smallIdx])
        if array[largeIdx] > array[largeIdx+1]:
            largestOutOfOrder = max(largestOutOfOrder, array[largeIdx])

    if smallestOutOfOrder == float('inf') and largestOutOfOrder == float('-inf'):
        return indices

    idx = 0
    while idx < len(array):
        if array[idx] > smallestOutOfOrder:
            indices[0] = idx
            break
        idx += 1

    idx = len(array) - 1
    while idx >= 0:
        if array[idx] < largestOutOfOrder:
            indices[1] = idx
            break
        idx -= 1

    return indices
