# O(n) time | O(n) space, where n is the length of the input array
def minRewards(scores):
    if len(scores) == 2:
        return 3

    rewards = [1] * len(scores)
    idx = 1

    while idx < len(scores) - 1:
        if scores[idx] < scores[idx - 1] and scores[idx] < scores[idx + 1]:
            lowerIdx = idx - 1
            upperIdx = idx + 1

            reward = 2
            while lowerIdx >= 0 and scores[lowerIdx] > scores[lowerIdx + 1] and reward > rewards[lowerIdx]:
                rewards[lowerIdx] = reward
                lowerIdx -= 1
                reward += 1

            reward = 2
            while upperIdx < len(scores) and scores[upperIdx] > scores[upperIdx - 1]:
                rewards[upperIdx] = reward
                upperIdx += 1
                reward += 1
            idx = upperIdx
            continue

        idx += 1

    return sum(rewards)
