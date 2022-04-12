from math import floor

def isPalindrome(string):
    check = floor(len(string)/2)

    for i in range(check):
        if string[i] != string[-1-i]:
            return False

    return True
