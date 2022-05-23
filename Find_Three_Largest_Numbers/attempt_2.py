# O(n) time | O(1) space

def findThreeLargestNumbers(array):
    highest = [array[i] for i in range(3)]
    highest.sort()

    if len(array) > 3:
        for i in range(3, len(array)):
            num = array[i]
            if num > highest[2]:
                # highest[0] = highest[1]
                # highest[1] = highest[2]
                shiftArray(highest, 2)
                highest[2] = num
            elif num > highest[1]:
                # highest[0] = highest[1]
                shiftArray(highest, 1)
                highest[1] = num
            elif num > highest[0]:
                highest[0] = num

    return highest


def shiftArray(array, idx):
    for i in range(idx):
        array[i] = array[i+1]
