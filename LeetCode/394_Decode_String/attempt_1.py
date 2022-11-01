# O(n) time | O(n) space
def decodeString(s):
    stack = []
    idx = 0
    
    for idx in range(len(s)):
        char = s[idx]
        
        if char != ']':
            stack.append(char)
            idx += 1
        else:
            substr = ""
            while stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()
            
            num = ""
            
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
        
            stack.append(int(num) * substr)
            
    return ''.join(stack)
