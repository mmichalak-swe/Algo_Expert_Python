# O(n^2) time | O(n) space, where n is the length of the input array
def threeNumberSum(array, targetSum):
    array.sort()
    output = []

    for i in range(len(array) - 2):
        leftPointer = i + 1
        rightPointer = len(array) - 1

        while leftPointer < rightPointer:
            currSum = array[i] + array[leftPointer] + array[rightPointer]
            if currSum == targetSum:
                output.append([array[i], array[leftPointer], array[rightPointer]])
                leftPointer += 1
                rightPointer -= 1
            elif currSum < targetSum:
                leftPointer += 1
            else:
                rightPointer -= 1

    return output
