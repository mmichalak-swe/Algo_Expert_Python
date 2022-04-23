def insertionSort(array):

    for i in range(1, len(array)):
        idx_curr = i
        idx_compare = i - 1
        curr = array[idx_curr]
        prev = array[idx_compare]
        
        while idx_curr > 0 and curr < prev:
            array[idx_compare], array[idx_curr] = curr, prev
            
            idx_curr -= 1
            curr = array[idx_curr]
            idx_compare -= 1
            prev = array[idx_compare]
            
    return array
