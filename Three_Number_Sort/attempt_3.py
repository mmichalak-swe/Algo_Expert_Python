# Copyright © 2022 AlgoExpert LLC. All rights reserved.
# 0(n) time | 0(1) space - where n is the length of the array

def threeNumberSort(array, order) :
    firstValue = order[0]
    secondValue = order[1]

    # Keep track of the indices where the values are stored
    firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1

    while secondIdx <= thirdIdx:
        value = array [secondIdx]

        if value == firstValue:
            array[secondIdx], array[firstIdx] = array[firstIdx], array[secondIdx]
            firstIdx += 1
            secondIdx += 1
        elif value == secondValue:
            secondIdx += 1
        else:
            array[secondIdx], array[thirdIdx] = array[thirdIdx], array[secondIdx]
            thirdIdx -= 1

    return array
