# O(n) time | O(1) space, where n is the length of the input array
def subarraySort(array):
    smallestOutOfOrder = float('inf')
    largestOutOfOrder = float('-inf')

    for i in range(1, len(array)):
        smallIdx = i
        largeIdx = len(array) - 1 - i
        if array[smallIdx] < array[smallIdx-1]:
            smallestOutOfOrder = min(smallestOutOfOrder, array[smallIdx])
        if array[largeIdx] > array[largeIdx+1]:
            largestOutOfOrder = max(largestOutOfOrder, array[largeIdx])

    if smallestOutOfOrder == float('inf') and largestOutOfOrder == float('-inf'):
        return [-1, -1]

    correctSmallIdx = 0
    while smallestOutOfOrder >= array[correctSmallIdx]:
        correctSmallIdx += 1
    correctLargeIdx = len(array) - 1
    while largestOutOfOrder <= array[correctLargeIdx]:
        correctLargeIdx -= 1

    return [correctSmallIdx, correctLargeIdx]
