class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # turn all numbers into int
        for index1, row in enumerate(board):
            empty_row = [".",".",".",".",".",".",".",".","."]
            for index2, item in enumerate(row):
                if item.isdigit():
                    empty_row[index2] = int(item)
                else:
                    continue
            board[index1] = empty_row
        
        # check if any rows have duplicates
        for row in board:
            number_check_rows = {}
            for item in row:
                if isinstance(item, int):
                    if item in number_check_rows:
                        return False
                    else:
                        number_check_rows[item] = 1

        # check if columns have duplicates
        number_check_cols = {}
        for i in range(9):
            for row in board:
                if row[i] in number_check_cols:
                    return False
                elif row[i] not in number_check_cols and isinstance(row[i], int):
                    number_check_cols[row[i]] = 1
                else:
                    continue
            number_check_cols = {}

        # check if squares have duplicates
        squares = {}
        for i in range(9):
            for j in range(9):
                if isinstance(board[i][j], int):
                    if (i // 3, j // 3) not in squares:
                        squares[i // 3, j // 3] = [board[i][j]]
                    else:
                        if board[i][j] not in squares[i // 3, j // 3]:
                            squares[i // 3, j // 3].append(board[i][j])
                        else:
                            return False
        return True




        