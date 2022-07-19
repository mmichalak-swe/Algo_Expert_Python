# O(n) time | O(1) space, where n is the length of the array
def moveElementToEnd(array, toMove):
    ptrOne = 0
    ptrTwo = len(array) - 1
    count = 1

    while ptrOne < ptrTwo:
        if array[ptrOne] != toMove:
            ptrOne += 1
        elif array[ptrTwo] == toMove:
            ptrTwo -= 1
        else:
            swap(array, ptrOne, ptrTwo)
            ptrOne += 1
            ptrTwo -= 1

    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
