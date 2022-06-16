# Recursive Solution
# O(2^(w+h) time | O(w+h) space, where w, h are width, height respectively
def numberOfWaysToTraverseGraph(width, height):
    if width == 1 or height == 1:
        return 1

    return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)
