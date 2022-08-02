# Brute-Force Solution
# O(n^2) time | O(1) space
def largestRectangleUnderSkyline(buildings):

    maxArea = 0

    for i in range(len(buildings)):
        minHeight = buildings[i]
        maxArea = max(maxArea, buildings[i])
        for j in range(i + 1, len(buildings)):
            minHeight = min(minHeight, buildings[j])
            currArea = ((j - i) + 1) * minHeight
            maxArea = max(maxArea, currArea)

    return maxArea
