# Optimal, non-optimzed solution
# O(1) time | O(1) space - max length of input array is 12
# max # of IP addresses is 2^32

def validIPAddresses(string):
    if len(string) < 4 or len(string) > 12:
        return []
    output = []

    for first in range(1, 4):
        firstNum = string[:first]
        if not firstNum or int(firstNum) > 255 or (len(firstNum) > 1 and firstNum[0] == '0'):
            break

        for second in range(1, 4):
            if first + second <= len(string):
                secondNum = string[first:first+second]
                if not secondNum or int(secondNum) > 255 or (len(secondNum) > 1 and secondNum[0] == '0'):
                    break

            for third in range(1, 4):
                if first + second + third <= len(string):
                    thirdNum = string[first+second:first+second+third]
                    if not thirdNum or int(thirdNum) > 255 or (len(thirdNum) > 1 and thirdNum[0] == '0'):
                        break

                fourthNum = string[first+second+third:]
                if not fourthNum or int(fourthNum) > 255 or (len(fourthNum) > 1 and fourthNum[0] == '0'):
                    continue

                output.append(firstNum + '.' + secondNum + '.' + thirdNum + '.' + fourthNum)
    
    return output
