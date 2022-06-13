# O(nd) time | O(n) space, d is # of denoms,
# n is len(waysChange) array, depends on argument n
def numberOfWaysToMakeChange(n, denoms):
    # need 0 as the base case (1 way to make 0, use 0 coins)
    waysChange = [0 for _ in range(n+1)]

    for denom in denoms:
        for amount in range(0, n+1):
            if amount == 0:
                waysChange[0] = 1  # only one way to make an amount of zero
            elif denom <= amount:
                waysChange[amount] += waysChange[amount - denom]

    return waysChange[-1]
