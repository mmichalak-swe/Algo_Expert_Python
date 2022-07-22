# O(n) time | O(n) space, where n is the # of values in the array
def spiralTraverse(array):
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0

    horizontal = len(array[0])
    vertical = len(array)

    numValues = horizontal * vertical
    x = 0
    y = -1

    spiral = []

    while numValues > 0:
        for i in range(horizontal):
            y += DIRECTIONS[direction][1]
            spiral.append(array[x][y])
            numValues -= 1
        horizontal -= 1
        direction += 1

        for i in range(vertical - 1):
            x += DIRECTIONS[direction][0]
            spiral.append(array[x][y])
            numValues -= 1
        vertical -= 1
        direction = direction + 1 if direction < 3 else 0

    return spiral
