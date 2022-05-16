# Upper Bound: O(n^2 * n!) time | O(n*n!) space
# Average: O(n*n!) time | O(n*n!) space

def getPermutations(array):
    perms = []
    permHelper(array, [], perms)
    return perms


def permHelper(array, perm, perms):

    if not (len(array)) and len(perm):
        perms.append(perm)
    
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPerm = perm + [array[i]]
            permHelper(newArray, newPerm, perms)


print(getPermutations([1, 2, 3]))