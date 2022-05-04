# O(n) time | O(1) space - n is len of input array

def kadanesAlgorithm(array):
    curr_max = array[0]
    max_at_idx = array[0]
    
    for i in range(1, len(array)):
        num = array[i]
        curr_max = max(num, curr_max + num)
        max_at_idx = max(curr_max, max_at_idx)
    return max_at_idx
