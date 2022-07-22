# O(n) time | O(n) space, where n is the # of values in the array
def spiralTraverse(array):
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    horizontal = len(array[0])
    vertical = len(array)

    spiral = []
    
    numValues = horizontal * vertical
    x = 0
    y = 0
    direction = 0

    while numValues > 0:
        for i in range(horizontal):
            spiral.append(array[x][y])
            y += DIRECTIONS[direction][1]
            numValues -= 1
        y -= DIRECTIONS[direction][1]
        direction += 1
        x += DIRECTIONS[direction][0]
        horizontal -= 1

        for i in range(vertical - 1):
            spiral.append(array[x][y])
            x += DIRECTIONS[direction][0]
            numValues -= 1
        x -= DIRECTIONS[direction][0]
        direction = direction + 1 if direction < 3 else 0
        y += DIRECTIONS[direction][1]
        vertical -= 1

    return spiral
