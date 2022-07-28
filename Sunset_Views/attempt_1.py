# O(n) time | O(n) space, where n is the length of the input array
def sunsetViews(buildings, direction):

    leftViews = []
    leftMax = float('-inf')
    rightViews = []
    rightMax = float('-inf')

    for i in range(len(buildings)):
        leftIdx = i
        rightIdx = len(buildings) - 1 - i

        if buildings[leftIdx] > leftMax:
            leftViews.append(leftIdx)
            leftMax = buildings[leftIdx]
        if buildings[rightIdx] > rightMax:
            rightViews.append(rightIdx)
            rightMax = buildings[rightIdx]
        
    return leftViews if direction == 'WEST' else list(reversed(rightViews))
