# AE Optimal Solution
# O(n) time | O(n) space, where n is the length of the input array
def largestRectangleUnderSkyline(buildings):
    stack = []
    maxArea = 0

    for idx, height in enumerate(buildings + [0]):
        while len(stack) != 0 and buildings[stack[-1]] >= height:
            buildingHeight = buildings[stack.pop()]
            length = idx if len(stack) == 0 else idx - stack[-1] - 1
            maxArea = max(maxArea, length * buildingHeight)

        stack.append(idx)

    return maxArea
