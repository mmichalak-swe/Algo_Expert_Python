# First Solution: O(3n) time | O(n) space
# Second Solution: O(n) time | O(n) space
# Solution #2 uses a stack and is the optimal solution

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: x[0])
        
        maxDefense = {}
        output = 0
        
        for character in properties:
            currentAttack = character[0]
            currentDefense = character[1]
            maxDefense[currentAttack] = max(character[1], maxDefense.get(character[0], float('-inf')))
        
        maxFromAbove = None
        for key in reversed(maxDefense.keys()):
            if maxFromAbove is None:
                maxFromAbove = maxDefense[key]
                maxDefense[key] = -1
            else:
                temp = maxDefense[key]
                maxDefense[key] = maxFromAbove
                maxFromAbove = max(maxFromAbove, temp)
            
        for character in properties:
            currentAttack = character[0]
            currentDefense = character[1]
            if maxDefense[currentAttack] != -1 and currentDefense < maxDefense[currentAttack]:
                output += 1
        
        return output

    
#         properties.sort(key=lambda x: (x[0], -x[1]))
        
#         print(properties)
        
#         stack = []
#         ans = 0
        
#         for a, d in properties:
#             print(stack)
#             while stack and stack[-1] < d:
#                 stack.pop()
#                 ans += 1
#             stack.append(d)
#         return ans
