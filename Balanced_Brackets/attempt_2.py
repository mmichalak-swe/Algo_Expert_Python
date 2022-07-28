# O(n) time | O(n) space
def balancedBrackets(string):
    openChars = '([{'
    closeChars = ')]}'
    match = {')': '(',
             ']': '[',
             '}': '{'}
    stack = []

    for char in string:
        if char in openChars:
            stack.append(char)
        elif char in closeChars:
            # account for trying to pop closed bracket when no open exists
            if len(stack) == 0:
                return False
            if stack[-1] == match[char]:
                stack.pop()
            else:
                return False

    # account for open brackets left on stack
    return len(stack) == 0
