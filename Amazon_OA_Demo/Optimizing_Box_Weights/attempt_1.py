def minimalHeaviestSetA(arr):
    arr.sort(reverse=True)
    sumWeights = sum(arr)
    subsetAWeight = 0
    subsetA = []

    for val in arr:
        subsetAWeight += val
        subsetA.append(val)
        sumWeights -= val

        if subsetAWeight > sumWeights:
            break

    return reversed(subsetA)
    
    ## FAILS ONE TEST CASE
    # arr.sort()
    # sumWeights = sum(arr)
    # subsetAWeight = 0

    # idx = 0
    # for i in range(len(arr)):
    #     val = arr[i]
    #     subsetAWeight += val
    #     sumWeights -= val

    #     if subsetAWeight > sumWeights:
    #         idx = i
    #         break

    # return arr[idx:]
