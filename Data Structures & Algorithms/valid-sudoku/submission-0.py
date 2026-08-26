class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate_box(x, y):
            d = {}
            for i in range(3):
                for j in range(3):
                    val = board[x+i][y+j]
                    if val == ".":
                        continue
                    d[val] = d.get(val, 0) + 1
            return not any(v > 1 for v in d.values())

        def validate_lines(x):
            dc, dr = {}, {}
            for i in range(len(board)):
                val_c = board[x][i]
                val_r = board[i][x]
                if val_c != ".":
                    dc[val_c] = dc.get(val_c, 0) + 1
                if val_r != ".":
                    dr[val_r] = dr.get(val_r, 0) + 1
            return not any(v > 1 for v in dc.values()) and not any(v > 1 for v in dr.values())

        for i in range(len(board)):
            if not validate_lines(i):
                return False

        for i in (0, 3, 6):
            for j in (0, 3, 6):  # fix here
                if not validate_box(i, j):
                    return False
        return True