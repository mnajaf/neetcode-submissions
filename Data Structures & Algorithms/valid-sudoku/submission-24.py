class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in board:
            check = set()
            for c in r:
                    if c != ".":
                        if c in check:
                            return False
                        check.add(c)

        for r in range(0,len(board),3):
            for c in range(0,len(board),3):
                check = set()
                for row in range(r,r + 3):
                    for col in range(c,c + 3):
                        if board[row][col] != ".":
                            if board[row][col] in check:
                                return False
                            check.add(board[row][col])
        


        for r in range(0,len(board)):
            check = set()
            for c in range(0,len(board)):
                if board[c][r] != ".":
                    if board[c][r] in check:
                        return False
                    check.add(board[c][r])
        return True
                  




        