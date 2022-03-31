# O(n) time, O(n) space

def sortedSquaredArray(array):
    result = [0 for num in array]
    left = 0
    right = len(array) - 1
	
    for i in reversed(range(len(array))):
        low = abs(array[left])
        high = abs(array[right])
		
        if high > low:
            result[i] = high ** 2
            right -= 1
        else:
            result[i] = low ** 2
            left += 1
	
    return result
