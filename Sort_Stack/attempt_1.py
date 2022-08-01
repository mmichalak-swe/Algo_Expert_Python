# O(n^2) time | O(n) space, where n is the length of the input array
def sortStack(stack):
    if not stack:
        return stack

    value = stack.pop()
    sortStack(stack)

    recursiveHelper(stack, value)
    
    return stack


def recursiveHelper(stack, value):
    if len(stack) == 0 or value >= stack[-1]:
        stack.append(value)
        return

    top = stack.pop()
    recursiveHelper(stack, value)
    stack.append(top)
