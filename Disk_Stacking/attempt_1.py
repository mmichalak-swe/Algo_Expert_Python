# O(n^2) time | O(n) space
def diskStacking(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    towers = [None for disk in disks]
    output = []

    maxHeight = 0
    maxHeightIdx = 0
    for i in range(len(disks)):
        currDisk = disks[i]
        for j in range(0, i):
            newDisk = disks[j]
            tempHeight = currDisk[2]

            if isValid(newDisk, currDisk):
                tempHeight += heights[j]
                if tempHeight > heights[i]:
                    heights[i] = tempHeight
                    towers[i] = j
        if heights[i] > maxHeight:
            maxHeight = heights[i]
            maxHeightIdx = i

    return buildOutput(disks, towers, maxHeightIdx)


def isValid(newDisk, currDisk):
    return newDisk[0] < currDisk[0] and newDisk[1] < currDisk[1] and newDisk[2] < currDisk[2]


def buildOutput(disks, towers, maxHeightIdx):
    output = []
    while maxHeightIdx is not None:
        output.append(disks[maxHeightIdx])
        maxHeightIdx = towers[maxHeightIdx]
    return list(reversed(output))
