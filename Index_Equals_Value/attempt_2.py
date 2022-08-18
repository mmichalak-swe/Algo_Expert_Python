# Optimized Solution
# O(log(n)) time | O(1) space
def indexEqualsValue(array):
    left = 0
    right = len(array) - 1
    idx = float('inf')

    while left <= right:
        middle = (left + right) // 2

        if array[middle] > middle:
            right = middle - 1
        elif array[middle] < middle:
            left = middle + 1
        else:
            idx = min(idx, middle)
            right = middle - 1

    return idx if idx != float('inf') else -1
