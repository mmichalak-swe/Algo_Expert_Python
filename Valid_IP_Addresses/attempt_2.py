# Optimal Method
# O(1) time | O(1) space - max length of input array is 12
# max # of IP addresses is 2^32

def validIPAddresses(string):
    output = []

    for first in range(1, 4):
        strFirstNum = string[:first]
        if not isValid(strFirstNum):
            break

        for second in range(1, 4):
            if first + second <= len(string):
                strSecondNum = string[first:first+second]
                if not isValid(strSecondNum):
                    break

            for third in range(1, 4):
                if first + second + third <= len(string):
                    strThirdNum = string[first+second:first+second+third]
                    if not isValid(strThirdNum):
                        break

                strFourthNum = string[first+second+third:]
                if not isValid(strFourthNum):
                    continue

                output.append(strFirstNum + '.' + strSecondNum + '.' + strThirdNum + '.' + strFourthNum)
    
    return output


def isValid(string):
    if not string or int(string) > 255:
        return False

    # Check for leading zeros
    return len(string) == len(str(int(string)))
