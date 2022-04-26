# O(n^2) time | O(1) space

def selectionSort(array):
	
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != i:
            swap(i, min_idx, array)
                
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
