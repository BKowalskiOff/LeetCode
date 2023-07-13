class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def canPlace(x: int, y: int, val: int):
            # check row and column
            for i in range(9):
                if board[y][i] == val or board[i][x] == val:
                    return False
            
            corner_x = 3*(x//3)
            corner_y = 3*(y//3)
            
            for i in range(corner_y, corner_y + 3):
                for j in range(corner_x, corner_x + 3):
                    if board[i][j] == val:
                        return False
            
            return True

        def solveFromPos(pos: int) -> None:
            while pos <= 80:
                x = pos%9
                y = pos//9
                if board[y][x] == '.':
                    placed = False
                    for val in range(1,10):
                        if canPlace(x, y, str(val)):
                            board[y][x] = str(val)
                            if solveFromPos(pos+1) == False:
                                board[y][x] = '.'
                            else:
                                placed = True
                    if not placed:
                        return False
                pos += 1
            return True

        solveFromPos(0)
