def kadanesAlgorithm(array):
    curr_max = 0
    curr_sum = 0
    
    for num in array:
        if num > curr_sum and curr_sum < 0:
            curr_max = num
            curr_sum += num
            continue

        if curr_sum + num > curr_max:
            curr_max += num

        curr_sum += num

    return curr_max
