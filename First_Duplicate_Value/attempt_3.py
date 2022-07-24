# Best Solution
# O(n) time | O(1) space
def firstDuplicateValue(array):
    for num in array:
        if array[abs(num) - 1] < 0:
            return abs(num)
        else:
            array[abs(num) - 1] *= -1

    return -1
