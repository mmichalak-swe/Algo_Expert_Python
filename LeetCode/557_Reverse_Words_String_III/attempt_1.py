# O(n * m) time | O(n) space, where n is the len of the input string,
# and m is the len of the longest word in the string
class Solution:
    def reverseWords(self, s: str) -> str:
#         s = s.split()
        
#         for i in range(len(s)):
#             s[i] = s[i][::-1]

#         return ' '.join(s)
            
        return ' '.join(x[::-1] for x in s.split())
