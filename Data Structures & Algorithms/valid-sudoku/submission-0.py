class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, sqrs = defaultdict(list), defaultdict(list), defaultdict(list)
        cursor = 0

        while cursor < 81:
            cur_row = cursor // 9
            cur_col = cursor % 9
            cur_sqr = (cur_row // 3) * 3 + (cur_col // 3)
            cursor += 1
            c = board[cur_row][cur_col]

            if c == ".":
                continue
            elif c not in rows[cur_row] and c not in cols[cur_col] and c not in sqrs[cur_sqr]:
                rows[cur_row].append(c)
                cols[cur_col].append(c)
                sqrs[cur_sqr].append(c)
            else:
                return False

        return True