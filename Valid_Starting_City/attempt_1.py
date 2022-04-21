# O(n^2) time | O(1) space

def validStartingCity(distances, fuel, mpg):
    num_of_cities = len(distances)

    for i in range(num_of_cities):
        if (fuel[i] * mpg < distances[i]):
            continue
        else:
            current_range = 0
            curr_city = i
            for j in range(i, i + num_of_cities):
                current_range += mpg * fuel[curr_city]
                current_range -= distances[curr_city]

                if current_range < 0:
                    break
                if j == num_of_cities - 1:
                    return i

                curr_city = (curr_city + 1) % num_of_cities

    return -1
