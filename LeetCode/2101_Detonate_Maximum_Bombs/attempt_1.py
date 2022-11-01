# O(n^3) time | O(n) space
# n^3 is worst case time complexity
class Solution:
    
    currDet = 0
    
    def maximumDetonation(self, bombs):
        
        def dfsHelper(b1, visited):
            if b1 in visited:
                return

            visited.add(b1)
            self.currDet += 1

            for b2 in range(len(bombs)):
                if b2 == b1:
                    continue
                if b2 not in visited and inRange(bombs[b1], bombs[b2]):
                    dfsHelper(b2, visited)

        # check whether center of b2 is within or equal to b1 radius
        def inRange(b1, b2):
            return math.dist((b1[0], b1[1]), (b2[0], b2[1])) <= b1[2]

        maxDet = 0
        for b1 in range(len(bombs)):
            self.currDet = 0
            visited = set()

            dfsHelper(b1, visited)

            maxDet = max(maxDet, self.currDet)
            
            # saves a lot of time if all bombs are used, immediately return
            if maxDet == len(bombs):
                return len(bombs)

        return maxDet
