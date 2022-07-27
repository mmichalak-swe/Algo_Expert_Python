# Brute-Force Solution
# O(n^4) time | O(n) space, where n is the length of the input array
def fourNumberSum(array, targetSum):
    output = []
    for a in range(len(array)):
        numOne = array[a]
        for b in range(a + 1, len(array)):
            numTwo = array[b]
            for c in range(b + 1, len(array)):
                numThree = array[c]
                for d in range(c + 1, len(array)):
                    numFour = array[d]
                    if numOne + numTwo + numThree + numFour == targetSum:
                        output.append([numOne, numTwo, numThree, numFour])
    return output
