def insertionSort(array):

    for i in range(1, len(array)):
        idx_curr = i
        idx_prev = i - 1
        
        while idx_curr > 0 and array[idx_curr] < array[idx_prev]:
            array[idx_prev], array[idx_curr] = array[idx_curr], array[idx_prev]
            
            idx_curr -= 1
            idx_prev -= 1
            
    return array
