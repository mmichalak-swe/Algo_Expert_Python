# O(n) time | O(n) space
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_Stack = []
        t_Stack = []
        
        r = len(s) if len(s) > len(t) else len(t)
        
        for i in range(r):
            if i < len(s):
                if s[i] != '#':
                    s_Stack.append(s[i])
                else:
                    if s_Stack:
                        s_Stack.pop()

            if i < len(t):
                if t[i] != '#':
                    t_Stack.append(t[i])
                else:
                    if t_Stack:
                        t_Stack.pop()
        
        return ''.join(s_Stack) == ''.join(t_Stack)
