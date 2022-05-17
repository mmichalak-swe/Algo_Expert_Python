# Works with all tests individually on AE, but not
# all together. Attempt 2 fixes everything

# O(4^n * n) time | O(4^n * n) space, where n is len of the phone number

def phoneNumberMnemonics(phoneNumber):
    string_digits = list(phoneNumber)

    return pNumberhelper(string_digits)


def pNumberhelper(string_digits, idx=0, result=[], curr = []):
    if idx == len(string_digits):
        result.append(''.join(curr))
        return result
    
    for char in DIGIT_LOOKUP[string_digits[idx]]:
        curr.append(char)
        pNumberhelper(string_digits, idx+1, result, curr)
        curr = curr[:idx]
    
    return result


DIGIT_LOOKUP = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}
