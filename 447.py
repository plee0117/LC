class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        booms = 0
        from collections import Counter
        for p in points:
            distance = list(map(lambda x: (x[0] - p[0]) ** 2 + (x[1] - p[1]) **2, points))
            c = Counter(distance)
            for v in c.values():
                if v > 1:
                    booms += v * (v - 1)
        return booms