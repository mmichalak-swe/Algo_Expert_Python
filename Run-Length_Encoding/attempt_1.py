# O(n) time, O(n) space, where n is the length of the input string


def runLengthEncoding(string):
    count = 0
    ans = []
    prev = string[0]

    for char in string:
        if char == prev and count == 9: # once a max of 9 in a row is reached, add to list
            ans.append(str(count))
            ans.append(prev)
            count = 1
            prev = char
            continue
        elif char == prev: # continue count if char is same as last
            count += 1
            prev = char
            continue
        else: # add count to list is char changes
            ans.append(str(count))
            ans.append(prev)
            prev = char
            count = 1

    # Handle the last character
    ans.append(str(count))
    ans.append(prev)

    return ("".join(ans))
