def insertionSort(array):

    for i in range(1, len(array)):
        curr = array[i]
        prev = array[i-1]
        
        if curr < prev:
            for j in range(i): # not a correct implementation of insertion sort
                if curr < array[j]:
                    array.pop(i)
                    array.insert(j, curr)
                    break
    return array
