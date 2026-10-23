class Solution:
    def row_col_check(self, board, check_type):
        for row in range(9):
            s = set()
            for col in range(9):
                num = board[row][col] if check_type == "row" else board[col][row]
                if num == ".":
                    continue
                if num in s:
                    return False
                else:
                    s.add(num)
        return True

    def check_sub_matrix(self, board, srow, scol):
        s = set()
        for row in range(srow, srow + 3):
            for col in range(scol, scol + 3):
                num = board[row][col]
                if num == ".":
                    continue
                if num in s:
                    return False
                else:
                    s.add(num)
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        if not self.row_col_check(board, "row"):
            # print("ROW")
            return False
        if not self.row_col_check(board, "col"):
            # print("COL")
            return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # print("ROW COL", i, j)
                if not self.check_sub_matrix(board, i, j):
                    return False
        return True
