class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    board[i][j] = "123456789"

        self.solve(board)
        self.printB(board)

    @staticmethod
    def solve(oldBoard: [[str]]) -> [[str]]:
        newBoard = [row[:] for row in oldBoard]

        if not Solution.reduceOptions(newBoard):
            return False
        
        Solution.printB(newBoard)

        for i in range(len(newBoard)):
            for j in range(len(newBoard[i])):
                cur = newBoard[i][j]
                if len(cur) > 1:
                    for tmp in cur:
                        newBoard[i][j] = tmp
                        if Solution.solve(newBoard):
                            Solution.copyB(newBoard, oldBoard)
                            return True
                    return False

        Solution.copyB(newBoard, oldBoard)
        return True

    @staticmethod
    def reduceOptions(oldBoard: [[str]]) -> [[str]]:
        newBoard = [row[:] for row in oldBoard]
        newSetValue = False
        for i in range(len(newBoard)):
            for j in range(len(newBoard[i])):
                curOptions = newBoard[i][j]
                if len(curOptions) > 1:
                    for m in range(len(newBoard[i])):
                        cur = newBoard[i][m]
                        if m is j:
                            continue
                        if len(cur) == 1 and cur in curOptions:
                            curOptions = curOptions.replace(cur, '', 1)

                    for n in range(len(newBoard[i])):
                        cur = newBoard[n][j]
                        if n is i:
                            continue
                        if len(cur) == 1 and cur in curOptions:
                            curOptions = curOptions.replace(cur, '', 1)

                    X = int(i / 3)
                    Y = int(j / 3)

                    for m in range(3):
                        for n in range(3):
                            convertedM = X * 3 + m
                            convertedN = Y * 3 + n
                            if convertedM is i and convertedN is j:
                                continue
                            cur = newBoard[convertedM][convertedN]
                            if len(cur) == 1 and cur in curOptions:
                                curOptions = curOptions.replace(cur, '', 1)
                    if curOptions == "":
                        return False
                    else:
                        newBoard[i][j] = curOptions
                        if len(curOptions) == 1:
                            newSetValue = True
        if newSetValue:
            Solution.reduceOptions(newBoard)
        Solution.copyB(newBoard, oldBoard)
        return True

    @staticmethod
    def copyB(board: [[str]], newBoard: [[str]]) -> [[str]]:
        for i in range(len(board)):
            for j in range(len(board[i])):
                newBoard[i][j] = board[i][j]


    @staticmethod
    def printB(board: [[str]]) -> [[str]]:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "":
                    print("[]", end= '   ')
                else:
                    print(board[i][j], end= '   ')
            print('\n')
        print('\n')
                    

val = [[".",".",".",".","8","7","3",".","."],[".","6","1",".",".",".","5",".","7"],["3",".",".","6",".","1",".","4","."],[".",".","2",".","7",".","4",".","1"],[".","8","3",".","4",".",".","6","."],[".",".",".",".","3","9",".",".","2"],[".",".","6",".",".",".","1",".","3"],[".",".",".",".",".",".","6","7","."],["9","1",".",".",".","3",".",".","."]]
tmp = Solution()
tmp.solveSudoku(val)



        
