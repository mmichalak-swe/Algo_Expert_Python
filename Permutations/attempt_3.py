# O(n*n!) time | O(n*n!) space

def getPermutations(array):
    perms = []
    permHelper(0, array, perms)
    return perms


def permHelper(i, array, perms):
    if i == len(array) - 1:
        perms.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i ,j)
            permHelper(i + 1, array, perms)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


print(getPermutations([1, 2, 3]))