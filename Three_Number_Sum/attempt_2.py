# O(n^2) time | O(n) space, where n is the length of the input array
# not 100% optimal due to sorting the input array, and then the output
def threeNumberSum(array, targetSum):
    array.sort()
    output = []

    for i in range(1, len(array) - 1):
        leftPointer = i - 1
        rightPointer = i + 1

        while leftPointer >= 0 and rightPointer < len(array):
            if array[leftPointer] + array[i] + array[rightPointer] == targetSum:
                output.append([array[leftPointer], array[i], array[rightPointer]])
                leftPointer -= 1
                rightPointer += 1
            elif array[leftPointer] + array[i] + array[rightPointer] < targetSum:
                rightPointer += 1
            else:
                leftPointer -= 1

    return sorted(output, key=lambda x: x[0])
