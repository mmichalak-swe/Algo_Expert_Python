# O(n) time | O(n) space, where n is the length of the input array
def arrayOfProducts(array):
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]
    for i in range(1, len(array)):
        leftIdx = i
        rightIdx = len(array) - 1 - i

        leftProducts[leftIdx] = leftProducts[leftIdx - 1] * array[leftIdx - 1]
        rightProducts[rightIdx] = rightProducts[rightIdx + 1] * array[rightIdx + 1]

    return [leftProducts[i] * rightProducts[i] for i in range(len(array))]
