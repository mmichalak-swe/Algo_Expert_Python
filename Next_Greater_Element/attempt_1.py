# Brute-Force Solution
# O(n^2) time | O(n) space
def nextGreaterElement(array):
    output = []

    for idx in range(len(array)):
        for j in range(1, len(array) + 1):
            newIdx = (idx + j) % len(array)
            if array[newIdx] > array[idx]:
                output.append(array[newIdx])
                break
            if newIdx == idx:
                output.append(-1)
                break
        
    return output
