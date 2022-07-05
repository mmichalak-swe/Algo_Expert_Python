# Non-Optimal Solution
# O(n*k*k) time | O(k) space, where n is length of the input array
# not great time complexity due to the removal of items in the array

def sortKSortedArray(array, k):
    output = []

    while len(array) > 0:
        localMin = []
        for i in range(k+1):
            if i < len(array):
                localMin.append(array[i])
        output.append(min(localMin))
        array.remove(min(localMin))
        
    return output
