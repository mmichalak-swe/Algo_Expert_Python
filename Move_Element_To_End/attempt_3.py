# O(n) time | O(n) space
# if we cannot modify input array
# implementing a deque would be more efficient, but function
# must return a list
def moveElementToEnd(array, toMove):
    output = []

    for num in array:
        if num != toMove:
            output.insert(0, num)
        else:
            output.append(num)

    return output
