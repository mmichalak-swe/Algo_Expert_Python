def underscorifySubstring(string, substring):
    locations = []

    for i in range(len(string)):
        end = i + len(substring) if i + (len(substring)) < len(string) else len(string)
        if string.find(substring, i, end) != -1:
            locations.append([i, end])
    
    if not locations:
        return string

    flatLocations = []

    if len(locations) == 1:
        flatLocations = [locations[0][0], locations[0][1]]
    else:
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

    output = []
    underIdx = 0
    for i in range(len(string)):
        if underIdx > len(flatLocations) - 1:
            output.append(string[i])
            continue
        
        if i == flatLocations[underIdx]:
            output.append('_')
            underIdx += 1

        output.append(string[i])

        if i == len(string) - 1 and underIdx == len(flatLocations) - 1:
            output.append('_')
    
    return ''.join(output)
