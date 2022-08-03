# Brute-Force Solution
# O(n^2) time | O(1) space
def largestRectangleUnderSkyline(buildings):

    maxArea = 0

    for i in range(len(buildings)):
        currHeight = buildings[i]

        leftIdx = i
        while leftIdx > 0 and buildings[leftIdx - 1] >= currHeight:
                leftIdx -= 1

        rightIdx = i
        while rightIdx < len(buildings) - 1 and buildings[rightIdx + 1] >= currHeight:
                rightIdx += 1
        
        currMaxArea = (rightIdx - leftIdx + 1) * currHeight
        maxArea = max(maxArea, currMaxArea, currHeight)

    return maxArea
