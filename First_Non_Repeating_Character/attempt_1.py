def firstNonRepeatingCharacter(string):

    checked = []

    for i in range(len(string)):
        char = string[i]

        if char in checked:
            continue

        count = 1

        for j in range(i+1, len(string)):
            if string[j] == char:
                count += 1

        if count == 1:
            return i
        else:
            checked.append(char)

    return -1
