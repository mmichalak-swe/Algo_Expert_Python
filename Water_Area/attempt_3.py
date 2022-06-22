# O(n) time | O(n) space, where n is the length of the input array
def waterArea(heights):
    maxes = [0 for _ in heights]

    leftMax = 0
    for idx, height in enumerate(heights):
        maxes[idx] = leftMax
        leftMax = max(leftMax, height)

    rightMax = 0
    waterDepth = 0
    for idx in reversed(range(len(heights))):
        height = heights[idx]
        minHeight = min(rightMax, maxes[idx])
        if height < minHeight:
            waterDepth += minHeight - height
        rightMax = max(rightMax, height)

    return waterDepth
