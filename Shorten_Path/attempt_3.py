# O(n) time | O(n) space, where n is the length of the path
def shortenPath(path):
    cleanPath = [token for token in path.split('/') if token not in ["", "."]]
    stack = [''] if path[0] == '/' else []

    for token in cleanPath:
        if token == '..':
            if len(stack) == 0 or stack[-1] == '..':
                stack.append(token)
            elif stack[-1] != '':
                stack.pop()
        else:
            stack.append(token)

    if len(stack) == 1 and stack[0] == '':
        return '/'

    return '/'.join(stack)
