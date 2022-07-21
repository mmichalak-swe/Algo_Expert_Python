def radixSort(array):
    if len(array) <= 1:
        return array

    maxDigit = len(str(max(array)))

    # must start at 0 for this solution to work, not 1
    for digit in range(0, maxDigit):
        array = countingSort(array, digit)

    return array


def countingSort(array, digit):
    sortedArray = [0] * len(array)
    counts = [0 for num in range(10)] # range of base number system

    digitColumn = 10 ** digit
    for num in array:
        numDigit = (num // digitColumn) % 10
        counts[numDigit] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for idx in range(len(array) - 1, -1, -1):
        numDigit = (array[idx] // digitColumn) % 10
        counts[numDigit] -= 1
        sortedArray[counts[numDigit]] = array[idx]
    
    return sortedArray
