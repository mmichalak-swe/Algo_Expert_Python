# O(n^2) time | O(1) space

def firstNonRepeatingCharacter(string):

    checked = []

    for i, char in enumerate(string):
        if char in checked:
            continue
        elif char not in string[i+1:]:
            return i

        checked.append(char)

    return -1
