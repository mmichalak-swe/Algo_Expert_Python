# O(n) time | O(1) space, where n len of input array
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]

    for i in range(len(array)):
        if i == 0:
            twoBack = array[0]
        elif i == 1:
            oneBack = max(twoBack, array[1])
        else:
            current = max(oneBack, array[i] + twoBack)
            twoBack = oneBack
            oneBack = current

    # need to return oneBack, not current, to account for
    # len(array) = 2
    return oneBack
