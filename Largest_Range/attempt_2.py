# O(n) time | O(n) space, where n is the length of the input array
def largestRange(array):
    visited = {}
    output = [0, 0]
    longestRun = 0

    for num in array:
        visited[num] = False

    for num in visited:
        if visited[num] == False:
            visited[num] = True
    
            lowerNum = num - 1
            upperNum = num + 1
            currentRun = 1
    
            while lowerNum in visited:
                visited[lowerNum] = True
                currentRun += 1
                lowerNum -= 1

            while upperNum in visited:
                visited[upperNum] = True
                currentRun += 1
                upperNum += 1

            if currentRun > longestRun:
                longestRun = currentRun
                output = [lowerNum + 1, upperNum - 1]

    return output
