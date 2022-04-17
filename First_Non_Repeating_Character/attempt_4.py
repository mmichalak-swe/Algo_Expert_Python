# O(n) time | O(1) space

def firstNonRepeatingCharacter(string):
    checked = {}

    for char in string:
        checked[char] = checked.get(char, 0) + 1

    for char in string:
        if checked[char] == 1:
            return string.index(char)

    return -1
