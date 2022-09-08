# O(n) time | O(n) space, where n is the length of the roman numeral
class Solution:
    def intToRoman(self, num: int) -> str:
        
        table = {1000: "M",
                 900: "CM",
                 500: "D",
                 400: "CD",
                 100: "C",
                 90: "XC",
                 50: "L",
                 40: "XL",
                 10: "X",
                 9: "IX",
                 5: "V",
                 4: "IV",
                 1: "I"}
        
        output = []
        
        for key in table:
            output.append((num // key) * table[key])
            num %= key
            
        return ''.join(output)
