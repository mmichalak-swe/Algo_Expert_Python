# O(n*log(n)) time | O(1) space, however, time complexity may be higher than O(n) due to
# re-sizing list, as elements are deleted
def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    
    idx = 0
    while idx < len(sortedIntervals) - 1:
        if sortedIntervals[idx][1] >= sortedIntervals[idx + 1][0]:
            sortedIntervals[idx][1] = max(sortedIntervals[idx][1], sortedIntervals[idx + 1][1])
            del sortedIntervals[idx + 1]
            continue
        else:
            idx += 1
    
    return sortedIntervals
