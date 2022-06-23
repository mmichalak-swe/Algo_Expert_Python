# O(ic) time | O(ic) space, where i is the number of items, c is the capacity
# equal to the number of items in the values array (i*c)
def knapsackProblem(items, capacity):
    values = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(values)):
        for j in range(1, len(values[i])):
            item = items[i - 1]
            value, weight = item[0], item[1]

            if weight <= j:
                values[i][j] = max(values[i-1][j], values[i-1][j-weight] + value)
            else:
                values[i][j] = values[i-1][j]

    idxs = []
    row = len(values) - 1
    col = len(values[row]) - 1

    while row > 0:
        if values[row][col] == values[row-1][col]:
            row -= 1
        else:
            idxs.append(row - 1)
            col -= items[row - 1][1]
            row -= 1
        if col == 0:
            break

    return [values[-1][-1], list(reversed(idxs))]
