def minimumWaitingTime(queries):
    queries.sort()
    idx = len(queries) - 1

    ans = 0

    while idx >= 0:
        for i in range(idx):
            ans += queries[i]
        idx -= 1

    return ans