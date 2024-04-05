class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        return self.get_row(rowIndex)

    def get_row(self, row_index: int) -> list[int]:
        row = [1] * (row_index + 1)
        for i in range(2, row_index + 1):
            for j in range(i // 2, 0, -1):
                row[j] = row[j] + row[j - 1]
            row[i // 2 + 1] = row[i // 2] if i % 2 else row[i // 2 - 1]
        for i in range(row_index, row_index // 2, -1):
            row[i] = row[row_index - i]
        return row
