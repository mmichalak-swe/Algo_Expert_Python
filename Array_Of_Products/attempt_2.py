# O(n) time | O(n) space, where n is the length of the input array
def arrayOfProducts(array):
    leftProducts = [array[0] for _ in range(len(array))]
    rightProducts = [array[len(array)-1] for _ in range(len(array))]
    for i in range(2, len(array)):
        leftIdx = i
        rightIdx = len(array) - 1 - i

        leftProducts[leftIdx] = leftProducts[leftIdx - 1] * array[leftIdx - 1]
        rightProducts[rightIdx] = rightProducts[rightIdx + 1] * array[rightIdx + 1]

    output = [rightProducts[0]]

    for i in range(1, len(array) - 1):
        output.append(leftProducts[i] * rightProducts[i])
    output.append(leftProducts[-1])

    return output
