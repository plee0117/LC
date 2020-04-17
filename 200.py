class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inCommon(a, l, common):
            found = 0
            for c in common:
                if a in c and l in c:
                    found = 1
                elif a in c:
                    c.add(l)
                    found = 1
                elif l in c:
                    c.add(a)
                    found = 1
            if not found:
                common.append({a, l})
            return common
        
        if grid:
            label = [[0] * len(grid[0]) for i in range(len(grid))]
        else:
            return 0
        islands = 0
        common = []
        for idx, r in enumerate(grid):
            for jdx, n in enumerate(r):
                if n == '1':
                    if jdx > 0:
                        left = label[idx][jdx - 1]
                    else:
                        left = 0
                    if idx > 0:
                        above = label[idx - 1][jdx]
                    else:
                        above = 0
                    if left > 0:
                        label[idx][jdx] = left
                        if above > 0 and above != left:
                            common = inCommon(above, left, common)
                    elif above > 0:
                        label[idx][jdx] = above
                    else:
                        label[idx][jdx] = int(n) + islands
                        islands += 1
        i = 0
        while i < len(common) - 1:
            j = len(common) - 1
            while i < j:
                if common[i].intersection(common[j]):
                    common[i].update(common[j])
                    common.pop(j)
                j -= 1
            i += 1
        reps = 0
        for i in common:
            reps += len(i)
        return islands - reps + len(common)