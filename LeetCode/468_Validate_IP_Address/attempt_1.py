# O(n) time | O(n) space
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        IPvFour = True if '.' in queryIP else False
        
        splitIP = queryIP.split('.') if IPvFour else queryIP.split(':')
        
        if IPvFour:
            if len(splitIP) != 4:
                return "Neither"

            for numStr in splitIP:
                try:
                    # check for leading zeroes, letters in numStr
                    if len(numStr) != len(str(int(numStr))):
                        return "Neither"

                    num = int(numStr)

                except ValueError:
                    return "Neither"
                
                if num > 255:
                    return "Neither"
        
            return "IPv4"
        
        else:
            if len(splitIP) != 8:
                return "Neither"

            for hexStr in splitIP:
                if not 1 <= len(hexStr) <= 4:
                    return "Neither"
                
                for char in hexStr:
                    if not char.isdigit() and not 97 <= ord(char.lower()) <= 102:
                        return "Neither"

            return "IPv6"
