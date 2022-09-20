# O(n^2) time | O(n) space, where n is length of input string
# worst case O(n) space, if entire input string is longest palindrome
# most efficient solution due to no extra slicing of string except 1 time at output
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getLongestPalindrome(string, leftIdx, rightIdx):
            while leftIdx >= 0 and rightIdx < len(string) and string[leftIdx] == string[rightIdx]:
                leftIdx -= 1
                rightIdx += 1
            return [leftIdx + 1, rightIdx]
        
        currentLongest = [0, 1]
        for i in range(1, len(s)):
            odd = getLongestPalindrome(s, i - 1, i + 1)
            even = getLongestPalindrome(s, i - 1, i)
            longest = max(odd, even, key=lambda x: x[1] - x[0])
            currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
        
        return s[currentLongest[0] : currentLongest[1]]
