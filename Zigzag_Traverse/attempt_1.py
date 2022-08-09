def zigzagTraverse(array):
    maxRow = len(array) - 1
    maxCol = len(array[0]) - 1
    row = 0
    col = 0
    directions = {'dL': [1, -1],
                  'uR': [-1, 1]}
    direction = 'dL'
    output = []

    while True:
        output.append(array[row][col])
        if row == maxRow and col == maxCol:
            break

        if direction == 'dL':
            if isValid(row + directions['dL'][0], col + directions['dL'][1], maxRow, maxCol):
                row += directions['dL'][0]
                col += directions['dL'][1]
            else:
                if row == maxRow:
                    col += 1
                    direction = 'uR'
                elif col == 0:
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
                elif row == 0:
                    col += 1
                    direction = 'dL'

    return output


def isValid(row, col, maxRow, maxCol):
    return 0 <= row <= maxRow and 0 <= col <= maxCol
