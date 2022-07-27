# Optimal Solution
# O(n^2) time | O(n^2) space, where n is the length of the input array
def fourNumberSum(array, targetSum):
    pairSums = {}
    output = []

    # first time through array doesn't add anything to pairSums
    for i in range(1, len(array)):
        numOne = array[i]
        for j in range(i + 1, len(array)):
            numTwo = array[j]
            currentSum = numOne + numTwo
            difference = targetSum - currentSum
            if difference in pairSums:
                for pair in pairSums[difference]:
                    output.append([pair[0], pair[1], numOne, numTwo])

        for k in range(0, i):
            newSum = numOne + array[k]
            if newSum in pairSums:
                pairSums[newSum].append([array[k], numOne])
            else:
                pairSums[newSum] = [[array[k], numOne]]
    
    return output
