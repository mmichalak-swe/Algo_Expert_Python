def isPalindrome(string):
    forward = 0
    back = len(string) - 1

    while (forward < back):
        if string[forward] != string[back]:
            return False
        
        forward += 1
        back -= 1

    return True
