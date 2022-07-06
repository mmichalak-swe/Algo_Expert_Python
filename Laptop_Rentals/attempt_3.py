# O(2*n*log(n) -> n*log(n)) time | O(2n - > n) space
def laptopRentals(times):
    if len(times) == 0:
        return 0

    startTimes = sorted([time[0] for time in times])
    endTimes = sorted([time[1] for time in times])

    startIdx = 0
    endIdx = 0

    while startIdx != len(times):
        # we need a new laptop
        if startTimes[startIdx] < endTimes[endIdx]:
            startIdx += 1
        # we can use an existing laptop
        else:
            startIdx += 1
            endIdx += 1
    
    return startIdx - endIdx
