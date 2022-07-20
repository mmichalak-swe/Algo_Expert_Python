# O(n) time | O(1) space, where n is the length of the input array
def isMonotonic(array):
    if len(array) <= 2:
        return True

    current = array[0]
    direction = None

    for i in range(1, len(array)):
        if array[i] < current:
            direction = 'decreasing' if not direction else direction
            if direction == 'increasing':
                return False
        elif array[i] > current:
            direction = 'increasing' if not direction else direction
            if direction == 'decreasing':
                return False
        else:
            continue
        current = array[i]

    return True
