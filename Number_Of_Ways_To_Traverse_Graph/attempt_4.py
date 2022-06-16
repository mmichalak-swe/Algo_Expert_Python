# BONUS Solution - Math Trick
# O(w + h) time | O(1) space
from math import factorial

def numberOfWaysToTraverseGraph(width, height):
    right = width - 1
    down = height - 1

    numerator = factorial(right + down)
    denominator = factorial(right) * factorial(down)

    return numerator / denominator
