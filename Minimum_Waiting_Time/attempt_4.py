# O(nlog(n)) Time | O(1) space

def minimumWaitingTime(queries):
    queries.sort()
    stop_len = len(queries) - 1
    total = 0

    for idx, time in enumerate(queries):
        queries_remaining = len(queries) - (idx + 1)
        total += time * queries_remaining

    return total
