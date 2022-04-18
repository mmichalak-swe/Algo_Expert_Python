def minimumWaitingTime(queries):
    queries.sort()
    idx = len(queries) - 1

    return recur_sum(queries, idx)

def recur_sum(query_list, n):
    if n == 0:
        return 0
    else:
        ans = 0
        for i in range(n):
            ans += query_list[i]

    return ans + recur_sum(query_list, n-1)
