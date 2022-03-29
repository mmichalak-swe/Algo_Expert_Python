# O(n^2) time, O(1) space

def twoNumberSum(array, targetSum):
    for i in range(len(array)):
            for j in range((i+1), len(array)):
                if array[i] + array[j] == targetSum:
                    return[array[i], array[j]]
    return[]
