# O(n) time | O(n) space, where n is the length of the input array
def waterArea(heights):
    leftMax = [0 for _ in heights]
    rightMax = [0 for _ in heights]

    # construct left and right max arrays
    for leftIdx in range(len(heights)):
        rightIdx = len(heights) - 1 - leftIdx

        if leftIdx == 0:
            continue
        leftMax[leftIdx] = max(heights[:leftIdx])
        rightMax[rightIdx] = max(heights[rightIdx+1:])

    waterDepth = 0
    for idx, height in enumerate(heights):
        if height < min(leftMax[idx], rightMax[idx]):
            waterDepth += min(leftMax[idx], rightMax[idx]) - heights[idx]

    return waterDepth
