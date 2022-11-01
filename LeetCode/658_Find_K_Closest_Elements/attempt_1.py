# O(n) time | O(1) space
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        
        low = 0
        high = len(arr) - 1

        while high - low >= k:
            if abs(arr[low] - x) > abs(arr[high] - x):
                low += 1
            else:
                high -= 1
                    
        return arr[low : high + 1]
