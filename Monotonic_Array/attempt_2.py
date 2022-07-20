# O(n) time | O(1) space, where n is the length of the input array
def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = None

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            direction = 'decreasing' if not direction else direction
            if direction == 'increasing':
                return False
        elif array[i] > array[i - 1]:
            direction = 'increasing' if not direction else direction
            if direction == 'decreasing':
                return False

    return True
