# O(n) time | O(n) space
def decodeString(s):
    stack, currNum, currString = [], 0, ""

    for c in s:
        if c == '[':
            stack.append(currString)
            stack.append(currNum)
            currString = ''
            currNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            currString = prevString + num*currString
        elif c.isdigit():
            currNum = currNum*10 + int(c)
        else:
            currString += c
    return currString
