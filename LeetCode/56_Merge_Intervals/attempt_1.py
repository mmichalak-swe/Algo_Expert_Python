class Solution:
    # O(n * log(n)) time | O(n) space, where n is the length of the input list
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0]) # O(n * log(n)) time
        
        output = [] # Worst case, O(n) space
        start = intervals[0][0]
        end = intervals[0][1]
        
        idx = 1
        while idx < len(intervals):
            if intervals[idx][0] <= end:
                end = max(end, intervals[idx][1])
                idx += 1
            else:
                output.append([start, end])
                start = intervals[idx][0]
                end = intervals[idx][1]
                
        output.append([start, end])
        
        return output
