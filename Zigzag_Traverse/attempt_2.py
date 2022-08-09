# O(n * m) time | O(n * m) space, where n * m is the number of elements in the input array
def zigzagTraverse(array):
    maxRow = len(array) - 1
    maxCol = len(array[0]) - 1
    row = 0
    col = 0
    directions = {'dL': [1, -1],
                  'uR': [-1, 1]}
    direction = 'dL'
    output = []

    while isValid(row, col, maxRow, maxCol):
        output.append(array[row][col])

        if direction == 'dL':
            if isValid(row + directions['dL'][0], col + directions['dL'][1], maxRow, maxCol):
                row += directions['dL'][0]
                col += directions['dL'][1]
            else:
                if row == maxRow:
                    col += 1
                    direction = 'uR'
                else:
                    row += 1
                    direction = 'uR'
    
        elif direction == 'uR':
            if isValid(row + directions['uR'][0], col + directions['uR'][1], maxRow, maxCol):
                row += directions['uR'][0]
                col += directions['uR'][1]
            else:
                if col == maxCol:
                    row += 1
                    direction = 'dL'
                else:
                    col += 1
                    direction = 'dL'

    return output


def isValid(row, col, maxRow, maxCol):
    return 0 <= row <= maxRow and 0 <= col <= maxCol
