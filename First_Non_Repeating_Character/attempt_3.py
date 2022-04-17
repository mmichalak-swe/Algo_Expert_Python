def firstNonRepeatingCharacter(string):
    checked = {}

    for char in string:
        if char not in checked:
            checked[char] = 1
        else:
            checked[char] += 1

    for char in string:
        if checked[char] == 1:
            return string.index(char)

    return -1
