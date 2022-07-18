# O(n^2) time | O(n^2) space, where n is the num of nodes in each input array, respectively
def sameBsts(arrayOne, arrayTwo):
    return sameBSTHelper(arrayOne, arrayTwo)


def sameBSTHelper(arrayOne, arrayTwo):
    arrayOneRoot = arrayOne[0] if arrayOne else None
    arrayTwoRoot = arrayTwo[0] if arrayTwo else None
    if len(arrayOne) != len(arrayTwo) or arrayOneRoot != arrayTwoRoot:
        return False

    # Not as optimal, adding comparison to loop through entire array
    if arrayOne == arrayTwo:
        return True

    arrayOneLeft = [num for num in arrayOne if num < arrayOne[0]]
    arrayTwoLeft = [num for num in arrayTwo if num < arrayTwo[0]]
    arrayOneRight = [arrayOne[i] for i in range(1, len(arrayOne)) if arrayOne[i] >= arrayOne[0]]
    arrayTwoRight = [arrayTwo[i] for i in range(1, len(arrayTwo)) if arrayTwo[i] >= arrayTwo[0]]

    return sameBSTHelper(arrayOneLeft, arrayTwoLeft) and sameBSTHelper(arrayOneRight, arrayTwoRight)
