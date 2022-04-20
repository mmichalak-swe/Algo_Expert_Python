# O(nLog(n)) time | O(1) space

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort() if fastest else redShirtSpeeds.sort(reverse=True)
    blueShirtSpeeds.sort(reverse=True)

    total_speed = 0

    for i in range(len(redShirtSpeeds)):
        red_rider = redShirtSpeeds[i]
        blue_rider = blueShirtSpeeds[i]
        total_speed += max(red_rider, blue_rider)

    return total_speed
