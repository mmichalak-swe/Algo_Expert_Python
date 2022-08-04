# Optimal Solution
# O(n) time | O(n) space, where n is the length of the input array
def largestRectangleUnderSkyline(buildings):
    buildings.append(0)
    idx = 0
    stack = []
    maxArea = 0

    while idx < len(buildings):
        if len(stack) == 0 or buildings[idx] > buildings[stack[-1]]:
            stack.append(idx)
            idx += 1
            continue

        currHeight = buildings[idx]

        while len(stack) > 0 and currHeight <= buildings[stack[-1]]:
            popHeight = buildings[stack.pop()]
            
            left = stack[-1] if len(stack) > 0 else -1
            right = idx

            currArea = popHeight * (right - left - 1)
            maxArea = max(maxArea, currArea)

        while len(stack) > 0 and buildings[stack[-1]] > buildings[idx]:
            stack.pop()

        stack.append(idx)
        idx += 1

    return maxArea
