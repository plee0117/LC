class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, l in enumerate(s):
            if l in d:
                d[l] = l
            else:
                d[l] = i
        print(d)
        m = -1
        for l in d:
            if type(d[l]) == str:
                pass
            elif m < 0:
                m = d[l]
            elif d[l] < m:
                m = d[l]
        return m