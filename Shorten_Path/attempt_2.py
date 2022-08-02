# O(n) time | O(n) space, where n is the length of the path
def shortenPath(path):
    pathType = 'absolute' if path[0] == '/' else 'relative'
    cleanPath = [token for token in path.split('/') if token not in ["", "."]]
    stack = []

    for token in cleanPath:
        if token == '..':
            if len(stack) == 0 or stack[-1] == '..':
                stack.append(token)
            if pathType == 'absolute' and len(stack) == 1:
                stack.pop()
            if len(stack) > 0 and stack[-1] != '..':
                stack.pop()
        else:
            stack.append(token)

    return '/'.join(stack) if pathType == 'relative' else '/' + '/'.join(stack)
