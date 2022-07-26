# O(n*log(n)) time | O(n) space, where n is the length of the input array
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    output = []
    
    idx = 0
    while idx < len(intervals):
        newStart = intervals[idx][0]
        newEnd = intervals[idx][1]
        if idx < len(intervals) - 1:
            while newEnd >= intervals[idx + 1][0]:
                newEnd = max(newEnd, intervals[idx + 1][1])
                idx += 1
                if idx == len(intervals) - 1:
                    break

        output.append([newStart, newEnd])
        idx += 1
    
    return output
