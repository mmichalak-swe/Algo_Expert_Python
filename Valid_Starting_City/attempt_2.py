# O(n) time | O(n) space

def validStartingCity(distances, fuel, mpg):

    entering_range_list = [0]
    curr_range = 0

    for i in range(len(distances) - 1):
        curr_range += (mpg * fuel[i] - distances[i])
        entering_range_list.append(curr_range)

    return entering_range_list.index(min(entering_range_list))
