# O(n) time | O(n) space, where n is the length of the input array
def minRewards(scores):
    rewards = [1 for score in scores]

    for idx in range(1, len(scores)):
        if scores[idx] > scores[idx - 1]:
            rewards[idx] += rewards[idx - 1]

    for idx in range(len(scores) - 2, -1, -1):
        if scores[idx] > scores[idx + 1]:
            rewards[idx] = max(rewards[idx], rewards[idx + 1] + 1)

    return sum(rewards)
