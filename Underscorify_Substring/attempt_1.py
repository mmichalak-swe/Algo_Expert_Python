def underscorifySubstring(string, substring):
    locations = []

    for i in range(len(string)):
        end = i + len(substring) if i + (len(substring)) < len(string) else len(string)
        if string.find(substring, i, end) != -1:
            locations.append([i, end])
    
    if not locations:
        return string

    flattenedLocations = []

    if len(locations) == 1:
        flattenedLocations = [locations[0][0], locations[0][1]]
    else:
        start = locations[0][0]
        end = locations[0][1]

        idx = 1
        while idx < len(locations):
            if locations[idx][0] <= end:
                end = locations[idx][1]
            else:
                flattenedLocations.append(start)
                flattenedLocations.append(end)
                start = locations[idx][0]
                end = locations[idx][1]

            if idx == len(locations) - 1:
                flattenedLocations.append(start)
                flattenedLocations.append(end)

                break

            idx += 1

    output = []
    underIdx = 0
    for i in range(len(string)):
        if underIdx > len(flattenedLocations) - 1:
            output.append(string[i])
            continue
        
        if i == flattenedLocations[underIdx]:
            output.append('_')
            underIdx += 1

        output.append(string[i])

        if i == len(string) - 1 and underIdx == len(flattenedLocations) - 1:
            output.append('_')
    
    return ''.join(output)
