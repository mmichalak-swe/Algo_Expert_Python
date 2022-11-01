# O(n) time | O(1) space
def backSpaceCompare(s, t):

    s = [char for char in s]
    t = [char for char in t]

    s_Ptr = 0
    t_Ptr = 0
    
    for i in range(len(s)):
        if s[i] == '#':
            s_Ptr -= 1
            s_Ptr = max(0, s_Ptr)
        else:
            s[s_Ptr] = s[i]
            s_Ptr += 1
    
    for i in range(len(t)):
        if t[i] == '#':
            t_Ptr -= 1
            t_Ptr = max(0, t_Ptr)
        else:
            t[t_Ptr] = t[i]
            t_Ptr += 1
    
    if s_Ptr != t_Ptr:
        return False
    
    for i in range(s_Ptr):
        if s[i] != t[i]:
            return False
    
    return True
