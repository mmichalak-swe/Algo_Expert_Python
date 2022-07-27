# Optimal Solution
# O(n^2) time | O(n^2) space, where n is the length of the input array
def fourNumberSum(array, targetSum):
    pairSums = {}
    output = []

    for i in range(len(array)):
        numOne = array[i]
        for j in range(i + 1, len(array)):
            numTwo = array[j]
            currentSum = numOne + numTwo
            difference = targetSum - currentSum
            if difference not in pairSums:
                continue
            else:
                for pair in pairSums[difference]:
                    output.append([pair[0], pair[1], numOne, numTwo])

        for k in range(0, i):
            newSum = numOne + array[k]
            if newSum in pairSums:
                pairSums[newSum].append([array[k], numOne])
            else:
                pairSums[newSum] = [[array[k], numOne]]
    
    return output
