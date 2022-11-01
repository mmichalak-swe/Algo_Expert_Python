# O(n) time | O(1) space
def minCost(colors, neededTime):
    maxCost = 0
    prev = 0

    idx = 1
    while idx < len(colors):
        if colors[idx] != colors[idx - 1]:
            prev = idx
        else:
            maxCost += min(neededTime[prev], neededTime[idx])
            if neededTime[prev] < neededTime[idx]:
                prev = idx
        idx += 1

    return maxCost
