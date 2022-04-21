# O(n^2) time | O(1) space

def validStartingCity(distances, fuel, mpg):

    for i in range(len(distances)):
        if (fuel[i] * mpg < distances[i]):
            continue
        else:
            current_range = 0
            curr_city = i
            for j in range(len(distances)):
                current_range += mpg * fuel[curr_city]
                current_range -= distances[curr_city]

                if current_range < 0:
                    break

                if j == len(distances) - 1:
                    return i

                if curr_city < len(distances) - 1:
                    curr_city += 1
                else:
                    curr_city = 0
