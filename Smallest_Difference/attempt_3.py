# O(2n + 2(n*log(n))) -> O(2*n*log(n)) time | O(1) space
# if arrays are different lengths, O(n*log(n) + m*log(m)) time
# if we could not mutate input arrays, space would be O(n + m)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    diff = float('inf')
    idxOne, idxTwo = 0, 0
    output = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        numOne, numTwo = arrayOne[idxOne], arrayTwo[idxTwo]
        currentDiff = abs(numOne - numTwo)

        if currentDiff == 0:
            return [numOne, numTwo]
        elif currentDiff < diff:
            diff = currentDiff
            output = [numOne, numTwo]

        if numOne < numTwo:
            idxOne += 1
        else:
            idxTwo += 1

    return output
