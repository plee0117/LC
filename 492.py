class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        best = [area, 1]
        w = 1
        upto = area ** (1/2) // 1
        while  w <= upto:
            if area % w == 0:
                l = area // w
                if l - w < best[0] - best[1]:
                    best = [l,w]
            w += 1
        return best