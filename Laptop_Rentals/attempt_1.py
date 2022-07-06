# Brute-Force Solution
# O(k*n) time | O(n) space, where n is the length of the times list,
# and k is the average interval length
def laptopRentals(times):
    intervals = {}
    numLaptops = 0
    for time in times:
        for i in range(time[0], time[1]):
            if i not in intervals:
                intervals[i] = 1
            else:
                intervals[i] += 1
            if intervals[i] > numLaptops:
                numLaptops = intervals[i]

    return numLaptops
