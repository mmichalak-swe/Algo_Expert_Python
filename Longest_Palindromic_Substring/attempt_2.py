# O(n) time | O(n) space
def longestPalindromicSubstring(string):
    long = ""
    for i in range(len(string)):
        temp = isPalindrome(i, string)
        if len(temp) > len(long):
            long = temp

    return long


def isPalindrome(idx, input):
    oddOffset = 0

    # odd length Palindrome logic
    while idx - oddOffset > 0 and idx + oddOffset < len(input):
        if input[idx - oddOffset] == input[idx + oddOffset]:
            oddOffset += 1
        else:
            break
    if 0 < idx < len(input):
        oddOffset -= 1
    
    l_offset = 1
    r_offset = 0

    # even length Palindrome logic
    while idx - l_offset > 0 and idx + r_offset < len(input):
        if input[idx-l_offset] == input[idx+r_offset]:
            l_offset += 1
            r_offset += 1
        else:
            break
    l_offset -= 1
    r_offset -= 1

    oddResult = input[idx-oddOffset : idx+oddOffset+1]
    evenResult = input[idx-l_offset : idx+r_offset+1]
    return max(oddResult, evenResult, key=len)

print(longestPalindromicSubstring("aca"))