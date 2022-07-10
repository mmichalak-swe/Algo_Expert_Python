# O(n + m) time | O(n) space, where n is the length of the input string, and
# m is the length of the substring
def underscorifySubstring(string, substring):
    locations = flatten(findLocations(string, substring))
    return underscore(string, locations)


def findLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx = nextIdx + 1
        else:
             break
    return locations


def flatten(locations):
    if not locations:
        return []
    if len(locations) == 1:
        return [locations[0][0], locations[0][1]]
    else:
        flatLocations = []
        start, end = locations[0][0], locations[0][1]
        idx = 1
        while idx < len(locations):
            if locations[idx][0] <= end:
                end = locations[idx][1]
            else:
                flatLocations.extend([start, end])
                start, end = locations[idx][0], locations[idx][1]

            if idx == len(locations) - 1:
                flatLocations.extend([start, end])
            idx += 1
    return flatLocations


def underscore(string, locations):
    output = []
    underIdx = 0
    for i in range(len(string)):
        if underIdx > len(locations) - 1:
            output.append(string[i:])
            break
        
        if i == locations[underIdx]:
            output.append('_')
            underIdx += 1

        output.append(string[i])

        if i == len(string) - 1 and underIdx == len(locations) - 1:
            output.append('_')
    
    return ''.join(output)
