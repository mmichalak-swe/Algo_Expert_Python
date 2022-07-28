# O(n) time | O(n) space, where n is the length of the input array
# using a stack
def sunsetViews(buildings, direction):

    views = []
    step = 1 if direction == 'EAST' else -1
    idx = 0 if direction == 'EAST' else len(buildings) - 1

    while idx >= 0 and idx < len(buildings):
        currHeight = buildings[idx]

        while len(views) > 0 and buildings[views[-1]] <= currHeight:
            views.pop()

        views.append(idx)
        idx += step
        
    return views if direction == 'EAST' else views[::-1]
