def shiftedBinarySearch(array, target):
    left = 0
    right = len(array) - 1
    middle = (left + right) // 2

    while left <= right:
        if array[middle] == target:
            return middle

        if array[left] <= array[middle]:
            if target < array[middle] and target >= array[left]:
                right = middle - 1
                middle = (left + right) // 2
            else:
                left = middle + 1
                middle = (left + right) // 2
        else: # array[left] > array[middle]
            if target > array[middle] and target <= array[right]:
                left = middle + 1
                middle = (left + right) // 2
            else:
                right = middle - 1
                middle = (left + right) // 2

    return -1
