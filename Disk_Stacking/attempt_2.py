# O(n^2) time | O(n) space
def diskStacking(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    towers = [None for disk in disks]
    output = []

    maxHeightIdx = 0
    for i in range(len(disks)):
        currDisk = disks[i]
        for j in range(0, i):
            newDisk = disks[j]

            if isValid(newDisk, currDisk):
                # Doesn't have to be >=, can just be >, >= signifies taking the most
                # recent stack with a certain height as you iterate
                if currDisk[2] + heights[j] >= heights[i]:
                    heights[i] = currDisk[2] + heights[j]
                    towers[i] = j
        if heights[i] > heights[maxHeightIdx]:
            maxHeightIdx = i

    return buildOutput(disks, towers, maxHeightIdx)


def isValid(nD, cD):
    return nD[0] < cD[0] and nD[1] < cD[1] and nD[2] < cD[2]


def buildOutput(disks, towers, idx):
    output = []
    while idx is not None:
        output.append(disks[idx])
        idx = towers[idx]
    return list(reversed(output))
