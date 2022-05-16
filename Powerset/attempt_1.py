# O(n*2^n) time | YIKES space

def powerset(array):
    ans = [[]]
    
    for i in range(len(array)):
        curr = ans[:]
        for item in curr:
            temp = item[:]
            temp.append(array[i])
            ans.append(temp)
    
    return ans
