# O(n) time | O(n) space, where n len of input array
def maxSubsetSumNoAdjacent(array):
    output = [0 for _ in range(len(array))]

    for i in range(len(array)):
        if i == 0:
            output[i] = array[i]
        elif i == 1:
            output[i] = max(array[0], array[1])
        else:
            oneBack = output[i-1]
            twoBack = output[i-2]

            output[i] = max(oneBack, array[i] + twoBack)

    # return max(output) if output else 0
    return output[-1] if output else 0
