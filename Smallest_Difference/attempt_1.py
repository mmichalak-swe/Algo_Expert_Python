def smallestDifference(arrayOne, arrayTwo):
    output = [None, None]
    diff = float('inf')

    for numOne in arrayOne:
        for numTwo in arrayTwo:
            if abs(numOne - numTwo) < diff:
                diff = abs(numOne - numTwo)
                output = [numOne, numTwo]
    return output
