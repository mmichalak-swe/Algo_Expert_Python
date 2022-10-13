def findTotalPower(power):
    # Write your code here
    # cache optimization power

    output = 0
    
    for i in range(len(power)):
        minVal = power[i]
        currSum = power[i]
        output += minVal * currSum
        for j in range(i + 1, len(power)):
            currSum += power[j]
            minVal = min(minVal, power[j])
            output += minVal * currSum
    
    return output
