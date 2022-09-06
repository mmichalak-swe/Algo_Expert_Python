# O(n) time | O(1) space
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxStreak = 1
        currStreak = 1
        direction = None
        
        for i in range(1, len(arr)):
            # if i == len(arr):
            #     maxStreak = max(currStreak, maxStreak)
            #     break
            
            if arr[i] > arr[i-1]:
                if direction == 'dec' or direction is None:
                    direction = 'inc'
                    currStreak += 1
                    continue
            elif arr[i] < arr[i-1]:
                if direction == 'inc' or direction is None:
                    direction = 'dec'
                    currStreak += 1
                    continue
            
            #streak is broken

            maxStreak = max(maxStreak, currStreak)
            currStreak = 2
            
            direction = 'inc' if arr[i] > arr[i-1] else 'dec'
            
            if arr[i] == arr[i-1]:
                direction = None
                currStreak = 1
                
        # calc maxStreak once more if streak continues to end of array
        maxStreak = max(maxStreak, currStreak)
        
        return maxStreak
