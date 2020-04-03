class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        from itertools import combinations
        works = []
        for comb in combinations(range(10), num):
            h = 0
            m = 0
            for n in range(4):
                if n in comb:
                    h += 2 ** n
            if h > 11:
                continue
            for n in range(4, 10):
                if n in comb:
                    m += 2 ** (n - 4)
            if m >= 60:
                continue
            if m < 10:
                m = '0' + str(m)
            else:
                m = str(m)
            works.append(str(h) + ':' + m)
        return works