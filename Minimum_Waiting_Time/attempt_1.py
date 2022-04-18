def minimumWaitingTime(queries):
    queries.sort()
    idx = len(queries) - 1

    return query_sum(queries, idx)


def query_sum(queries, n):
    ans = 0

    while n >= 0:
        for i in range(n):
            ans += queries[i]
        n -= 1
    return ans