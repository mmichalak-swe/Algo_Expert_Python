# O(n*2^n) time | O(n*2^n) space

def powerset(array):
    subsets = [[]]
    
    for num in array:
        for i in range(len(subsets)):
            curr = subsets[i]
            subsets.append(curr + [num])

    return subsets
