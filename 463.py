class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        w = len(grid[0])
        h = len(grid)
        def isAtEdge(x,y):
            if x >= h or x < 0:
                return True
            elif y >= w or y <0:
                return True
            elif grid[x][y] == 0:
                return True
            else:
                return False
        peri = 0
        for j in range(w):
            for i in range(h):
                if grid[i][j] == 1:
                    neighbors = [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]
                    peri += sum(isAtEdge(*n) for n in neighbors)
        return peri