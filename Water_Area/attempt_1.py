# O(n) time | O(n) space
def waterArea(heights):
    leftMax = [0 for _ in range(len(heights))]
    rightMax = [0 for _ in range(len(heights))]
    waterDepths = [0 for _ in range(len(heights))]

    # construct left and right max arrays
    for leftIdx in range(len(heights)):
        rightIdx = len(heights) - 1 - leftIdx

        if leftIdx == 0:
            continue
        leftMax[leftIdx] = max(heights[:leftIdx])
        rightMax[rightIdx] = max(heights[rightIdx+1:])

    for idx, height in enumerate(heights):
        if height < min(leftMax[idx], rightMax[idx]):
            waterDepths[idx] = min(leftMax[idx], rightMax[idx]) - heights[idx]

    return sum(waterDepths)
