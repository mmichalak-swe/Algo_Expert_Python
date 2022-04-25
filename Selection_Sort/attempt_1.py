def selectionSort(array):
    curr_min = 0
    swapped = True
    
    for i in range(len(array)):
        curr_min = array[i]
        min_idx = i
        swapped = False
        for j in range(i+1, len(array)):
            if array[j] < curr_min:
                min_idx = j
                curr_min = array[j]
                swapped = True
        if swapped:
            swap(i, min_idx, array)
                
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
