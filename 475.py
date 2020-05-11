class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        biggest = 0
        jdx = 0
        last = len(heaters) - 1
        for house in houses:
            while house > heaters[jdx]:
                if jdx < last:
                    jdx += 1
                else:
                    return max(biggest, houses[-1] - heaters[-1])
            if jdx == 0:
                temp = heaters[jdx] - house
            else:
                temp = min(house - heaters[jdx - 1], heaters[jdx] - house)
            biggest = max(biggest, temp)
        return biggest