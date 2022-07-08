# Brute-Force Solution
# O(n^2) time | O(n) space, where n is the length of the string
def longestSubstringWithoutDuplication(string):
    maxSubstring = (0, 0)
    for i in range(len(string)):
        uniqueChars = {string[i]: True}
        startIdx = i
        endIdx = i + 1
        for j in range(i+1, len(string)):
            if string[j] not in uniqueChars:
                uniqueChars[string[j]] = True
                endIdx += 1
            else:
                break

        maxSubstring = (startIdx, endIdx) if endIdx - startIdx > maxSubstring[1] - maxSubstring[0] else maxSubstring

    return string[maxSubstring[0]:maxSubstring[1]]
