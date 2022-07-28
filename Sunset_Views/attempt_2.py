# O(n) time | O(n) space, where n is the length of the input array
def sunsetViews(buildings, direction):

    views = []
    maxHeight = float('-inf')
    step = 1 if direction == 'WEST' else -1
    idx = 0 if direction == 'WEST' else len(buildings) - 1

    while idx >= 0 and idx < len(buildings):

        if buildings[idx] > maxHeight:
            views.append(idx)
            maxHeight = buildings[idx]

        idx += step
        
    return views if direction == 'WEST' else list(reversed(views))
