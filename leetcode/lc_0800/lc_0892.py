class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        return self.surface_area(grid)

    def surface_area(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        area = 0
        for i in range(m):
            for j in range(n):
                h = grid[i][j]
                if h == 0:
                    continue
                area += 2  # Top and bottom
                # The other four side faces
                area += h if i == 0 else max(0, h - grid[i - 1][j])
                area += h if i == m - 1 else max(0, h - grid[i + 1][j])
                area += h if j == 0 else max(0, h - grid[i][j - 1])
                area += h if j == n - 1 else max(0, h - grid[i][j + 1])
        return area
