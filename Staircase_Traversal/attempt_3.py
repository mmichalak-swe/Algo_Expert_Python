# O(n) time | O(n) space

def staircaseTraversal(height, maxSteps):
    currentNumOfWays = 0
    waysToTop = [1]
    
    for currentHeight in range(1, height + 1):
        startOfWindow = currentHeight - maxSteps - 1
        endOfWindow = currentHeight - 1
        
        if startOfWindow >= 0:
            currentNumOfWays -= waysToTop[startOfWindow]
        
        currentNumOfWays += waysToTop[endOfWindow]
        waysToTop.append(currentNumOfWays)
    
    return waysToTop[height]


print(staircaseTraversal(4, 2))