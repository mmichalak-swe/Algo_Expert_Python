# O(n) time | O(min(n, a)) space, where n is the len of the input string, and a is the
# length of the alphabet used to create the string (unique letters only)
def longestSubstringWithoutDuplication(string):
    lastPosition = {}
    longestSubstring = (0, 1)
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastPosition:
            startIdx = max(startIdx, lastPosition[char] + 1)

        if (i + 1) - startIdx > longestSubstring[1] - longestSubstring[0]:
            longestSubstring = (startIdx, i + 1)

        lastPosition[char] = i

    return string[longestSubstring[0] : longestSubstring[1]]
