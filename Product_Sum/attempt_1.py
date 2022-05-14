def productSum(array):
    return productSumhelper(array, depth=1)


def productSumhelper(array, depth):

    sum = 0

    for item in array:
        if type(item) is int:
            sum += item
        else:
            sum += productSumhelper(item, depth+1)

    return sum * depth
