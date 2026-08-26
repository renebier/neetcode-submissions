class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_col = defaultdict(set)
        set_row = defaultdict(set)
        boxes = defaultdict(set)

        box_idx = lambda x,y : (x // 3) * 3 + (y // 3)

        for i in range(len(board)):
            for j in range(len(board[1])):
                val = board[i][j]
                box = box_idx(i,j)
                if val == ".":
                    continue
                if val in set_col[i] or val in set_row[j] or val in boxes[box]:
                    return False
                set_col[i].add(val)
                set_row[j].add(val)
                boxes[box].add(val)

        return True