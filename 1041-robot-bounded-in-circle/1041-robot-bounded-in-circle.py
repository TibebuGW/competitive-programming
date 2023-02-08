class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        i = 0
        
        
        for char in instructions:
            if char == "G":
                pos[0] += direction[i][0]
                pos[1] += direction[i][1]
            elif char == "L":
                i = (i + 1)%4
            else:
                if i == 0:
                    i = 3
                else:
                    i -= 1
        
        return pos == [0, 0] or i != 0