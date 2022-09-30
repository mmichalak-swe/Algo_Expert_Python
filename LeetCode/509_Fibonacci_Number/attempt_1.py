class Solution:
    def fib(self, n: int) -> int:
        
#         def recursiveHelper(num):
#             if num == 0:
#                 return 0
#             if num == 1:
#                 return 1
            
#             return recursiveHelper(num - 1) + recursiveHelper(num - 2)
        
#         return recursiveHelper(n)

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        p1 = 0
        p2 = 1
        
        for i in range(n):
            temp = p1 + p2
            p1 = p2
            p2 = temp
            
        return p1
