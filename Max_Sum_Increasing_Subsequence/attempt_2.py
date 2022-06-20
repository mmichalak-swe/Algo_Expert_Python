# O(n^2) time | O(n) space, where n is the length of the input array
def maxSumIncreasingSubsequence(array):
    sums = array[:]
    seqs = [None for _ in array]
    maxSumIdx = 0

    for i in range(len(array)):
        currNum = array[i]
        for j in range(0, i):
            otherNum = array[j]

            if otherNum < currNum and sums[j] + currNum >= sums[i]:
                sums[i] = sums[j] + currNum
                seqs[i] = j

            if sums[i] >= sums[maxSumIdx]:
                maxSumIdx = i

    print(sums)
    print(seqs)
    return [sums[maxSumIdx], buildSequence(array, seqs, maxSumIdx)]


def buildSequence(array, seqs, idx):
    seq = []
    while idx is not None:
        seq.append(array[idx])
        idx = seqs[idx]
    return list(reversed(seq))
