from math import floor

def binarySearch(array, target):
    left_idx = 0
    right_idx = len(array) - 1
    
    while left_idx <= right_idx:
        mid_idx = floor((left_idx + right_idx)/2)

        if target < array[mid_idx]:
            right_idx = mid_idx - 1
        elif target > array[mid_idx]:
            left_idx = mid_idx + 1
        else:
            return mid_idx
    
    return -1
