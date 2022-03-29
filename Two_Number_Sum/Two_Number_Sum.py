def twoNumberSum(array, targetSum):
    ans = []
    for i in range(len(array)):

        try:
            for j in range((i+1), len(array)):
                if array[i] + array[j] == targetSum:
                    ans.append(array[i])
                    ans.append(array[j])
                    return ans
        except IndexError:
            return []
        return []

x = [3, 5, -4, 8, 11, 1, -1, 6]
y = 10

print(twoNumberSum(x,y))
