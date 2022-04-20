def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort() if fastest else redShirtSpeeds.sort(reverse=True)
    blueShirtSpeeds.sort(reverse=True)

    total_speed = 0

    for i in range(len(redShirtSpeeds)):
        if redShirtSpeeds[i] > blueShirtSpeeds[i]:
            total_speed += redShirtSpeeds[i]
        else:
            total_speed += blueShirtSpeeds[i]

    return total_speed
