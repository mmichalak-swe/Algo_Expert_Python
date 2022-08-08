# O(n) time | O(n) space, where n is the length of the input array
def largestRange(array):
    if len(array) == 1:
        return [array[0], array[0]]

    visited = {}
    output = [0, 0]

    for num in array:
        visited[num] = False

    for num in visited:
        if visited[num] == False:
            visited[num] = True
    
            lowerNum = num - 1
            upperNum = num + 1
    
            while lowerNum in visited and visited[lowerNum] == False:
                visited[lowerNum] = True
                lowerNum -= 1
            lowerNum += 1

            while upperNum in visited and visited[upperNum] == False:
                visited[upperNum] = True
                upperNum += 1
            upperNum -= 1

            if upperNum - lowerNum > output[1] - output[0]:
                output = [lowerNum, upperNum]

    return output
