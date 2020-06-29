class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        hlim = len(M[0])
        vlim = len(M)
        out = []
        from itertools import product
        from statistics import mean
        for y in range(vlim):
            out.append([])
            up = max(y - 1, 0)
            down = min(y + 2, vlim)
            for x in range(hlim):
                left = max(x - 1, 0)
                right = min(x + 2, hlim)
                neighbors = product(range(up, down), range(left, right))
                out[y].append(int(mean(map(lambda q: M[q[0]][q[1]], neighbors))))
        return out