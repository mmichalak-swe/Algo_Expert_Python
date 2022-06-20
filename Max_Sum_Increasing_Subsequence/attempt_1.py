# O(n^2) time | O(n) space, where n is the length of the input array
def maxSumIncreasingSubsequence(array):
    # worst case, greatest sum at each index is equal to value in array
    # make copy to initialize
    sums = [num for num in array]
    seqs = [None for _ in range(len(array))]
    maxSumIdx = 0

    for endIdx in range(len(array)):
        currIdx = 0
        sum = 0
        while currIdx <= endIdx:
            if array[currIdx] < array[endIdx] and sums[currIdx] + array[endIdx] >= sums[endIdx]:
                sums[endIdx] = sums[currIdx] + array[endIdx]
                seqs[endIdx] = currIdx
            currIdx += 1

        maxSumIdx = endIdx if sums[endIdx] >= sums[maxSumIdx] else maxSumIdx

    output = [sums[maxSumIdx], []]
    while maxSumIdx is not None:
        output[1].append(array[maxSumIdx])
        maxSumIdx = seqs[maxSumIdx]
    output[1].reverse()

    return output
