def productSum(array):
    return productSumhelper(array, sum=0, depth=1)


def productSumhelper(array, depth, sum=0):

    for item in array:
        if type(item) is int:
            sum += depth*item
        else:
            sum += productSumhelper(item, (depth*(depth+1)))

    return sum
