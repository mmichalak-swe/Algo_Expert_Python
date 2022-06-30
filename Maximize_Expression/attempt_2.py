# Optimal Solution
# O(4n) - > O(n) time | O(4n) -> O(n) space, where n is length of the input array
def maximizeExpression(array):
    if len(array) < 4:
        return 0

    maxA = [float('-inf') for num in array]    # max A
    maxAB = [float('-inf') for num in array]   # max A - B
    maxABC = [float('-inf') for num in array]  # max A - B + C
    maxABCD = [float('-inf') for num in array] # max A - B + C - D

    for i, num in enumerate(array):
        if i == 0:
            maxA[i] = num
        else:
            maxA[i] = max(maxA[i-1], num)

        if i >= 1:
            maxAB[i] = max(maxAB[i-1], maxA[i-1] - num)
        if i >= 2:
            maxABC[i] = max(maxABC[i-1], maxAB[i-1] + num)
        if i >= 3:
            maxABCD[i] = max(maxABCD[i-1], maxABC[i-1] - num)

    return  maxABCD[-1]
