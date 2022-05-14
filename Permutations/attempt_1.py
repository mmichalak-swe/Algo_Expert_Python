from itertools import permutations

def getPermutations(array):
    if not array:
        return []
    else:
        return list(permutations(array))
