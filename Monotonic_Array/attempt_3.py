# O(n) time | O(1) space, where n is the length of the input array
def isMonotonic(array):
    increasingOrEqual = True
    decreasingOrEqual = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            increasingOrEqual = False
        if array[i] > array[i - 1]:
            decreasingOrEqual = False

    return increasingOrEqual or decreasingOrEqual
