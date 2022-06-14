# O(nd) time | O(n) space, where n is n, or num of amounts from 0 to n inclusive,
# and d is # of denoms
def minNumberOfCoinsForChange(n, denoms):
    amounts = [float("inf") for _ in range(n+1)]
    amounts[0] = 0

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                amounts[amount] = min(amounts[amount], 1 + amounts[amount - denom])

    return amounts[n] if amounts[n] != float("inf") else -1
