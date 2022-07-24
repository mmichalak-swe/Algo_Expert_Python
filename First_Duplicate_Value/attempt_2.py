# Optimized solution
# O(n) time | O(n) space
def firstDuplicateValue(array):
    found = {}

    for num in array:
        if num in found:
            return num
        found[num] = True

    return -1
