# Optimized Solution
# O(log(n)) time | O(1) space
def indexEqualsValue(array):
    left = 0
    right = len(array) - 1
    firstIdx = float('inf')

    while left <= right:
        middle = (left + right) // 2

        if array[middle] > middle:
            right = middle - 1
        elif array[middle] < middle:
            left = middle + 1
        else:
            firstIdx = min(firstIdx, middle)
            if middle - 1 >= 0 and array[middle - 1] >= middle - 1:
                right = middle - 1
            else:
                break

    return firstIdx if firstIdx != float('inf') else -1
