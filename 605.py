class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zs = 0
        for idx, f in enumerate(flowerbed):
            if idx == 0 and f == 0:
                zs = 2
            elif f == 0:
                zs += 1
            elif zs:
                n -= (zs - 1) // 2
                zs = 0
                if n <= 0:
                    return True
        if zs > 0:
            n -= (zs) // 2
        return n <= 0 