# O(n^3) time | O(n) space
def longestPalindromicSubstring(string):
    long = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            current = string[i : j+1]
            if isPalindrome(current) and len(current) > len(long):
                long = current

    return long


def isPalindrome(current):
    return current == current[::-1]
