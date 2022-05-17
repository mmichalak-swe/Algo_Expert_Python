# Update logic to not have to clear curr,
# and not return result from helper which was
# causing incorrect output on AE

# O(4^n * n) time | O(4^n * n) space, where n is len of the phone number

def phoneNumberMnemonics(phoneNumber):
    string_digits = list(phoneNumber)
    curr = ['0'] * len(phoneNumber)
    res = []

    pNumberhelper(string_digits, curr, 0, res)
    return res


def pNumberhelper(string_digits, curr, idx=0, result=[]):
    if idx == len(string_digits):
        result.append(''.join(curr))
        return
    else:
        for char in DIGIT_LOOKUP[string_digits[idx]]:
            curr[idx] = char
            pNumberhelper(string_digits, curr, idx+1, result)


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

print(phoneNumberMnemonics("1905"))