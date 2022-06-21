# O(n^2) time | O(n) space, where n is the length of the input array
def minNumberOfJumps(array):
    numJumps = [float('inf') for _ in array]

    for i in range(len(array)):
        if i == 0:
            numJumps[0] = 0

        for j in range(1, array[i] + 1):
            if i + j < len(array):
                numJumps[i + j] = numJumps[i] + 1 if numJumps[i] + 1 < numJumps[i + j] else numJumps[i + j]
            else:
                break

    return numJumps[-1]
