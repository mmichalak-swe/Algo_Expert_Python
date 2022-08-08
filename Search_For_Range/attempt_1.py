# Non-Optimal
# Worst: O(n) time | O(1) space
# Average: O(log(n)) time | O(1) space
def searchForRange(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2

        if array[middle] < target:
            start = middle + 1
        elif array[middle] > target:
            end = middle - 1
        else:
            startRange = endRange = middle
            while startRange >= 0 and array[startRange] == target:
                startRange -= 1
            while endRange < len(array) and array[endRange] == target:
                endRange += 1

            return [startRange + 1, endRange - 1]

    return [-1, -1]
