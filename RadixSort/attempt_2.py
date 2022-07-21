# O(d(n+b)) time | O(n + b) space, where d is the num of digits,
# in the largest number in the array. n is the length of the input array
# b is the num of digits in the number system (in this case, 10 (base 10))
def radixSort(array):
    if len(array) <= 1:
        return array

    maxDigit = len(str(max(array)))

    for digit in range(1, maxDigit + 1):
        array = countingSort(array, digit)

    return array


def countingSort(array, digit):
    sortedArray = [0] * len(array)
    counts = [0 for num in range(10)] # range of base number system

    for num in array:
        strNum = str(num)
        try:
            numDigit = int(strNum[-digit])
        except IndexError:
            numDigit = 0
        counts[numDigit] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for num in list(reversed(array)):
        strNum = str(num)
        try:
            numDigit = int(strNum[-digit])
        except IndexError:
            numDigit = 0
        counts[numDigit] -= 1
        sortedArray[counts[numDigit]] = num
    
    return sortedArray
