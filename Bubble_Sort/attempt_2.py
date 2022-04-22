# Best: O(n) time | O(1) space  --- when array is ordered already, time will be O(n)
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space

def bubbleSort(array):

    swapPerformed = True
    counter = 0           # optimizes time efficiency slightly

    while(swapPerformed):
        swapPerformed = False
        for i in range(len(array) - 1 - counter):
            curr = array[i]
            next = array[i+1]

            if curr > next:
                array[i], array[i+1] = next, curr
                if not swapPerformed: swapPerformed = True
        counter += 1

    return array
