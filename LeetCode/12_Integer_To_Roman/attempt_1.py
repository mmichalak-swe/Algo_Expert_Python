# O(n) time | O(n) space, where n is the length of the roman numeral
class Solution:
    def intToRoman(self, num: int) -> str:
        
        output = []
        
        while num > 0:
            while num >= 1000:
                output.append("M")
                num -= 1000
            if 900 <= num < 1000:
                output.append("CM")
                num -= 900
            if 500 <= num < 900:
                output.append("D")
                num -= 500
            if 400 <= num < 500:
                output.append("CD")
                num -= 400
            while 100 <= num < 400:
                output.append("C")
                num -= 100
            if 90 <= num < 100:
                output.append("XC")
                num -= 90
            if 50 <= num < 90:
                output.append("L")
                num -= 50
            if 40 <= num < 50:
                output.append("XL")
                num -= 40
            while 10 <= num < 40:
                output.append("X")
                num -= 10
            if num == 9:
                output.append("IX")
                break
            if 5 <= num < 9:
                output.append("V")
                num -= 5
            if num == 4:
                output.append("IV")
                break
            while 1 <= num < 4:
                output.append("I")
                num -= 1
        
        return ''.join(output)
