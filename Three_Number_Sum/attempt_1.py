# O(n^3 time) | O(n) space, where n is the length of the input array
# Worst case O(3n) space, drop the constant and arrive at O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    output = []

    for i in range(len(array)):
        numOne = array[i]
        for j in range(i+1, len(array)):
            numTwo = array[j]
            for k in range(j+1, len(array)):
                numThree = array[k]

                if numOne + numTwo + numThree == targetSum:
                    output.append([numOne, numTwo, numThree])

    return output
