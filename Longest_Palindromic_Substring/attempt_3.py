# O(n^2) time | O(n) space, where n is length of input string
# worst case O(n) space, if entire input string is longest palindrome
# most efficient solution due to no extra slicing of string except 1 time at output
def longestPalindromicSubstring(string):
    long = [0, 1]
    for i in range(len(string)):        # O(n^2) time
        temp = isPalindrome(i, string)
        long = max(long, temp, key=lambda x: x[1] - x[0])

    return string[long[0]:long[1]]


def isPalindrome(idx, input):
    oddOffset = 1
    l_offset = 1
    r_offset = 0
    if 1 <= idx < len(input):
        while True:
            if idx - oddOffset >= 0 and idx + oddOffset < len(input) and input[idx - oddOffset] == input[idx + oddOffset]:
                oddOffset += 1
            else:
                oddOffset -= 1
                break

        while True:
            if idx - l_offset >= 0 and idx + r_offset < len(input) and input[idx - l_offset] == input[idx + r_offset]:
                l_offset += 1
                r_offset += 1
            else:
                l_offset -= 1
                r_offset -= 1
                break

        oddPal = [idx-oddOffset, idx+oddOffset+1]
        evenPal = [idx-l_offset, idx+r_offset+1]

        return max(oddPal, evenPal, key=lambda x: x[1] - x[0])
    else:
        return [idx, idx+1]
