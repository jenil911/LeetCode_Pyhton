class Solution:
    @staticmethod
    def backtracking(board: List[List[str]], row: int, col: int, rows_values: List[Set[str]], cols_values:List[Set[str]], row_col_values: List[List[Set[str]]]) -> True:
        if row == 9:
            return True
        if col == 9:
            return Solution.backtracking(board, row + 1, 0, rows_values, cols_values, row_col_values)
        if board[row][col] != ".":
            return Solution.backtracking(board, row, col + 1, rows_values, cols_values, row_col_values)
        for digit in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if not digit in rows_values[row] and not digit in cols_values[col] and not digit in row_col_values[row//3][col//3]:
                board[row][col] = digit
                rows_values[row].add(digit)
                cols_values[col].add(digit)
                row_col_values[row//3][col//3].add(digit)

                if Solution.backtracking(board, row, col+1, rows_values, cols_values, row_col_values):
                    return True
                board[row][col] = "."
                rows_values[row].remove(digit)
                cols_values[col].remove(digit)
                row_col_values[row//3][col//3].remove(digit)
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows_values: List[Set[str]] = [set() for _ in range(9)]
        cols_values:List[Set[str]] = [set() for _ in range(9)] 
        row_col_values: List[List[Set[str]]] = [
            [set() for _ in range(9)] 
            for _ in range(9)
        ]
        for row in range(9):
            for col in range(9):
                digit = board[row][col] 
                if digit != ".":
                    rows_values[row].add(digit)
                    cols_values[col].add(digit)
                    row_col_values[row//3][col//3].add(digit)
        
        for row in range(9):
            for col in range(9):
                digit = board[row][col] 
                if digit == ".":
                    self.backtracking(board, row, col, rows_values, cols_values, row_col_values)