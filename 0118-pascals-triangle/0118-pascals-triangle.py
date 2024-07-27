class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prev_rows = self.generate(numRows - 1)
        prev_row = prev_rows[-1]
        current_row = [1]

        for i in range(1, numRows - 1):
            current_row.append(prev_row[i - 1] + prev_row[i])

        current_row.append(1)
        prev_rows.append(current_row)

        return prev_rows