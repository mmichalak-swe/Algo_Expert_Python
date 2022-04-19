# O(nLog(n)) time | O(1) space

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    back_row = ""
    if redShirtHeights[0] > blueShirtHeights[0]:
        back_row = "red"
    else:
        back_row = "blue"

    if back_row == "red":
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
    else:
        for i in range(len(blueShirtHeights)):
            if blueShirtHeights[i] <= redShirtHeights[i]:
                return False
	
    return True
