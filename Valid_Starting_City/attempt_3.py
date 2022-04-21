# O(n) time | O(1) space

from copy import deepcopy

def validStartingCity(distances, fuel, mpg):

    min_range = 0
    city = 0
    range_left = 0

    for i in range(len(distances) - 1):
        range_left += (mpg * fuel[i]) - distances[i]
        if range_left < min_range:
            min_range = deepcopy(range_left)
            city = i + 1

    return city
