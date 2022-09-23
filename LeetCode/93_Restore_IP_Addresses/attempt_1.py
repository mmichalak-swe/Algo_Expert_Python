# O(1) time | O(1) space - max length of input array is 12
# max # of IP addresses is 2^32
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(string):
            if not string or int(string) > 255:
                return False
            
            # check for leading zeroes
            return len(string) == len(str(int(string)))

        output = []
        # filter out input that won't lead any valid results
        if not 4 <= len(s) <= 12:
            return output

        for first in range(1, 4):
            strFirstNum = s[:first]
            if not isValid(strFirstNum):
                break

            for second in range(1, 4):
                if first + second <= len(s):
                    strSecondNum = s[first:first+second]
                    if not isValid(strSecondNum):
                        break

                for third in range(1, 4):
                    if first + second + third <= len(s):
                        strThirdNum = s[first+second:first+second+third]
                        if not isValid(strThirdNum):
                            break

                    strFourthNum = s[first+second+third:]
                    if not isValid(strFourthNum):
                        continue

                    output.append(strFirstNum + '.' + strSecondNum + '.' + strThirdNum + '.' + strFourthNum)

        return output
