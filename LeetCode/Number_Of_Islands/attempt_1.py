DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def numIslands(grid):
    output = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '1':
                output += 1
                stack = [(row, col)]
                while stack:
                    newRow, newCol = stack.pop()
                    grid[newRow][newCol] = '2'
                    for direction in DIRECTIONS:
                        potentialRow = newRow + direction[0]
                        potentialCol = newCol + direction[1]
                        if not (0 <= potentialRow < len(grid)) or not (0 <= potentialCol < len(grid[0])):
                            continue
                        if grid[potentialRow][potentialCol] == '1':
                            stack.append((potentialRow, potentialCol))
            else:
                continue
                
    return output
