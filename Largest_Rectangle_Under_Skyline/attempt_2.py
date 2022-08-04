# Brute-Force Solution
# O(n^2) time | O(1) space
def largestRectangleUnderSkyline(buildings):

    maxArea = 0

    for i in range(len(buildings)):
        currHeight = buildings[i]
        maxArea = max(maxArea, currHeight)

        leftIdx = i
        while leftIdx > 0:
            if buildings[leftIdx - 1] >= currHeight:
                leftIdx -= 1
            else:
                break

        rightIdx = i
        while rightIdx < len(buildings) - 1:
            if buildings[rightIdx + 1] >= currHeight:
                rightIdx += 1
            else:
                break
        
        currMaxArea = (rightIdx - leftIdx + 1) * currHeight
        maxArea = max(maxArea, currMaxArea)

    return maxArea
