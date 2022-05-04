# O(n^2) time | O(1) space

def threeNumberSort(array, order):
    
    firstIdx = 0
    for i in range(len(array)):
        if array[i] == order[0]:
            swap(array, i, firstIdx)
            firstIdx += 1

    midIdx = firstIdx
    for i in range(midIdx, len(array)):
        if array[i] == order[1]:
            swap(array, i, midIdx)
            midIdx += 1

    return array


def swap(array, idx_1, idx_2):
    array[idx_1], array[idx_2] = array[idx_2], array[idx_1]
    return array
