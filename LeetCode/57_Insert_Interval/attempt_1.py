# O(n) time | O(1) space
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                output.append(interval)
            else:
                if interval[0] > newInterval[1]:
                    return output + [newInterval] + intervals[i:]
                else:
                    newInterval[0] = min(newInterval[0], interval[0])
                    newInterval[1] = max(newInterval[1], interval[1])
        
        return output + [newInterval]
