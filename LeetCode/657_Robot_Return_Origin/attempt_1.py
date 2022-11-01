# O(n) time | O(1) space
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # if len(moves) is odd, can't return to origin
        if len(moves) & 1:
            return False

        directions = {"U": (0, 1),
                      "R": (1, 0),
                      "D": (0, -1),
                      "L": (-1, 0)}
        
        x, y = 0, 0
        
        for move in moves:
            x += directions[move][0]
            y += directions[move][1]
            
        return x == y == 0
