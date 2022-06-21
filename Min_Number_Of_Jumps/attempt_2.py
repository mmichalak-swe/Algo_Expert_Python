# O(n) time | O(1) space, where n is the length of the input array
def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    # farthest index that can be reached
    farthest = array[0]
    # store number of jumps 'consumed' at a given index
    numJumps = 0
    # steps remaining until we need to consume another jump
    steps = array[0]

    for idx in range(1, len(array) - 1):
        if idx + array[idx] > farthest:
            farthest = idx + array[idx]

        steps -= 1

        if steps == 0:
            numJumps += 1
            steps = farthest - idx
    
    return numJumps + 1
