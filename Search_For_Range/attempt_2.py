# Optimal (Iterative)
# O(log(n)) time | O(1) space
def searchForRange(array, target):
    output = [-1, -1]
    searchForRangeHelper(array, target, 0, len(array) - 1, output, 'left')
    searchForRangeHelper(array, target, 0, len(array) - 1, output, 'right')
    return output


def searchForRangeHelper(array, target, start, end, output, direction):
    while start <= end:
        middle = (start + end) // 2

        if array[middle] < target:
            start = middle + 1
        elif array[middle] > target:
            end = middle - 1
        else:
            if direction == 'left':
                if middle == 0 or array[middle - 1] != target:
                    output[0] = middle
                    return
                else:
                    end = middle - 1
            else:
                if middle == len(array) - 1 or array[middle + 1] != target:
                    output[1] = middle
                    return
                else:
                    start = middle + 1
