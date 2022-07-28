# O(n) time | O(n) space
def balancedBrackets(string):
    match = {'(': ')',
             '[': ']',
             '{': '}'}
    stack = []

    for char in string:
        if char in match.keys():
            stack.append(char)
        elif char in match.values():
            # account for trying to pop closed bracket when no open exists
            if len(stack) == 0:
                return False
            if match[stack.pop()] == char:
                continue
            else:
                return False

    # account for open brackets left on stack
    return len(stack) == 0
