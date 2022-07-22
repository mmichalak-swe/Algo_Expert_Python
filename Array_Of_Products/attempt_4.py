# O(n) time | O(n) space, where n is the length of the input array
def arrayOfProducts(array):
    output = [1 for _ in range(len(array))]
    for leftIdx in range(1, len(array)):
        output[leftIdx] = output[leftIdx - 1] * array[leftIdx - 1]

    print(output)

    rightProduct = 1
    for rightIdx in range(len(array) - 1, -1, -1):
        output[rightIdx] *= rightProduct
        rightProduct *= array[rightIdx]

    return output
