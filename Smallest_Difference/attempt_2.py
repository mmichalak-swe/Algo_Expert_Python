def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne)
    print(arrayTwo)

    diff = float('inf')
    idxOne = 0
    idxTwo = 0
    numOne = arrayOne[0]
    numTwo = arrayTwo[0]

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        currentDiff = abs(arrayOne[idxOne] - arrayTwo[idxTwo])
        if currentDiff == 0:
            return [arrayOne[idxOne], arrayTwo[idxTwo]]
        elif currentDiff <= diff:
            diff = currentDiff
            if arrayOne[idxOne] < arrayTwo[idxTwo]:
                idxOne += 1
            else:
                idxTwo += 1
        else:
            idxOne = idxOne + 1 if arrayOne[idxOne] < arrayTwo[idxTwo] else idxOne
            idxTwo = idxTwo + 1 if arrayTwo[idxTwo] < arrayOne[idxOne] else idxTwo

x = [-1, 5, 10, 20, 28, 3]
y = [26, 134, 135, 15, 17]

print(smallestDifference(x, y))
