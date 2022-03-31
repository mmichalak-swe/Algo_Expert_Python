# O(n*log(n)) time, O(n) space

def sortedSquaredArray(array):
    result = [0 for num in array]

    for i in range(len(array)):
        result[i] = array[i] ** 2
	
    result.sort()
    return result

print(sortedSquaredArray([-2, -1]))