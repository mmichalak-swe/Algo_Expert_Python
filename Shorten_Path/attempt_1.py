# O(n) time | O(n) space, where n is the length of the path
def shortenPath(path):
    pathType = 'absolute' if path[0] == '/' else 'relative'
    cleanPath = [token for token in path.split('/') if token not in ["", "."]]
    stack = []
    
    if pathType == 'relative':
        for token in cleanPath:
            if token == '..' and len(stack) != 0:
                if stack[-1] != '..':
                    stack.pop()
                    continue

            stack.append(token)

    elif pathType == 'absolute':
        for token in cleanPath:
            if len(stack) == 0 and token == '..':
                    continue
            elif len(stack) != 0 and token == '..':
                if stack[-1] != '..':
                    stack.pop()
                    continue

            stack.append(token)

    return '/'.join(stack) if pathType == 'relative' else '/' + '/'.join(stack)
