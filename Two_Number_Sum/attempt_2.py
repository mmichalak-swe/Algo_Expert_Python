# O(n) time, O(n) space

def twoNumberSum(array, targetSum):
    
	ans = {}
	
	for num in array:
		if targetSum - num in ans:
			return [num, targetSum - num]
		else:
			ans[num] = True
	return []
