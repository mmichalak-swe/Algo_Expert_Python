# # O(k^n) time | O(n) space

# def staircaseTraversal(height, maxSteps):
# 	if height <= 1:
# 		return 1
    
# 	ways = 0
    
# 	for step in range(1, min(maxSteps, height) + 1):
# 		ways += staircaseTraversal(height - step, maxSteps)
    
# 	return ways

# ******** with MEMOIZATION ********

# O(k * n) time | O(n) space

def staircaseTraversal(height, maxSteps):
    return waysToTop(height, maxSteps, {0: 1, 1: 1})

def waysToTop(height, maxSteps, memoize):
    if height in memoize:
        return memoize[height]
    
    ways = 0
    
    for step in range(1, min(maxSteps, height) + 1):
        ways += waysToTop(height - step, maxSteps, memoize)
    
    memoize[height] = ways
    
    return ways
