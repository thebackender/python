#https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            vert = []
            horz = []
            for j in range(9):
                if board[j][i] != ".":
                    vert.append(board[j][i])
                if board[i][j] != ".":
                    horz.append(board[i][j])
            if len(vert) != len(set(vert)) or len(horz) != len(set(horz)):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                arr = []
                for k in range(3):
                    for l in range(3):
                        if board[i+k][l+j] != ".":
                            arr.append(board[i+k][l+j])
                if len(arr) != len(set(arr)):
                    return False
        return True
print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))