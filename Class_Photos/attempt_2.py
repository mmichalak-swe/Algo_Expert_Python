def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    back_row = "red" if redShirtHeights[0] > blueShirtHeights[0] else "blue"

    for i in range(len(redShirtHeights)):
        if back_row == "red":
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        else:
            if blueShirtHeights[i] <= redShirtHeights[i]:
                return False

    return True
