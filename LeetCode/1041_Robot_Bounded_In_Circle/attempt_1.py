# O(n) time | O(1) space
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        facing = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        xPos = 0
        yPos = 0
        direction = 0
        
        for instruction in instructions:
            if instruction == 'G':
                xPos += facing[direction][0]
                yPos += facing[direction][1]
            elif instruction == 'L':
                direction -= 1
            elif instruction == 'R':
                direction += 1

            direction %= 4
        
        return (xPos, yPos) == (0, 0) or direction != 0
        
        # if not xPos and not yPos: # hasn't moved
        #     return True
        # else:
        #     if direction:         # moved and direction changed
        #         return True
        #     else:                 # moved and direction didn't change
        #         return False
