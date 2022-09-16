# O(n*log(d)) time | O(1) space, where d is the difference between the max weight,
# and the sum of weights (the input array), n is the len of the input array
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            capacity = (left + right) // 2
            currentWeight = 0
            currentDays = 1
            
            for weight in weights:
                if currentWeight + weight > capacity:
                    currentDays += 1
                    currentWeight = weight
                else:
                    currentWeight += weight
            
            if currentDays <= days:
                right = capacity
            elif currentDays > days:
                left = capacity + 1
        
        return left
