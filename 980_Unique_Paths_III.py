class Solution:
    def uniquePathsIII(self, grid: [[int]]) -> int:
        
        """
        -1 - not fair game tile
        0 - fair game tile
        1 - start
        2 - end
        """

        numPaths = self.findPaths(grid, 0)
        print(numPaths)
        return numPaths

    @staticmethod
    def findPaths(grid, numPaths):

        if Solution.canFinish(grid) and not Solution.tilesLeft(grid): 
            return numPaths + 1

        moves = Solution.findMoves(grid)
        if moves:
            if moves[0]: #Up
                newGrid = Solution.move(grid, 'Up')
                numPaths = Solution.findPaths(newGrid, numPaths)
            if moves[1]: #Down
                newGrid = Solution.move(grid, 'Down')
                numPaths = Solution.findPaths(newGrid, numPaths)
            if moves[2]: #Left
                newGrid = Solution.move(grid, 'Left')
                numPaths = Solution.findPaths(newGrid, numPaths)
            if moves[3]: #Right
                newGrid = Solution.move(grid, 'Right')
                numPaths = Solution.findPaths(newGrid, numPaths)
        return numPaths

    """ Returns new grid with newly assigned start and and old start blocked off """
    @staticmethod
    def move(grid, direction):
        newGrid = [row[:] for row in grid]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:

                    newGrid[i][j] = -1
                    if direction == 'Up':
                        newGrid[i-1][j] = 1
                    elif direction == 'Down':
                        newGrid[i+1][j] = 1
                    elif direction == 'Left':
                        newGrid[i][j-1] = 1
                    else: #direction == 'Right'
                        newGrid[i][j+1] = 1
        
        return newGrid

    """
    Returns a boolean array with true false values corresponding to each possible movement
    Ex. [Up, Down, Left, Right]
        [0, 1, 1, 1]
        This means we can move in any direction beside up
    """
    @staticmethod
    def findMoves(grid) -> [bool]:
        moves = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    try:
                        if i-1 < 0:
                            raise IndexError
                        if grid[i-1][j] == 0:
                            moves.append(True)
                        else:
                            moves.append(False)
                    except IndexError:
                        moves.append(False)

                    try:
                        if grid[i+1][j] == 0:
                            moves.append(True)
                        else:
                            moves.append(False)
                    except IndexError:
                          moves.append(False)

                    try:
                        if j-1 < 0:
                            raise IndexError
                        if grid[i][j-1] == 0:
                            moves.append(True)
                        else:
                            moves.append(False)
                    except IndexError:
                          moves.append(False)

                    try:
                        if grid[i][j+1] == 0:
                            moves.append(True)
                        else:
                            moves.append(False)
                    except IndexError:
                          moves.append(False)

                    if not any(moves):
                        return False
                    else:
                        return moves

    """ Checking if end tile is next to start tile """
    @staticmethod
    def canFinish(grid) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    try:
                        if i-1 < 0:
                            raise IndexError
                        if grid[i-1][j] == 2:
                            return True
                    except IndexError:
                        pass

                    try:
                        if grid[i+1][j] == 2:
                            return True
                    except IndexError:
                        pass

                    try:
                        if j-1 < 0:
                            raise IndexError
                        if grid[i][j-1] == 2:
                            return True
                    except IndexError:
                        pass  

                    try:
                        if grid[i][j+1] == 2:
                            return True
                    except IndexError:
                        pass

                    return False

    """ Checking if there are any tiles on the board that could still be moved on """
    @staticmethod
    def tilesLeft(grid) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    return True
        return False

    """ Copies grid into empty array """
    @staticmethod
    def copyGrid(grid: [[str]], newGrid: [[str]]) -> [[str]]:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                newGrid[i][j] = grid[i][j]

val = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
tmp = Solution()
tmp.uniquePathsIII(val)