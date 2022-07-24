# Brute-Force Solution
# O(n^2) time | O(1) space
def firstDuplicateValue(array):
    minIndex = float('inf')

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                minIndex = min(minIndex, j)

    return array[minIndex] if minIndex != float('inf') else -1
