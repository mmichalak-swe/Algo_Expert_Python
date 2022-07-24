# Optimized solution
# O(n) time | O(n) space
def firstDuplicateValue(array):
    found = {}

    for num in array:
        if num not in found:
            found[num] = True
        else:
            return num

    return -1
