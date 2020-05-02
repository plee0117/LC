class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        sl = len(s)
        if sl == 0:
            return 0
        cookie = 0
        for idx, child in enumerate(g):
            while child > s[cookie]:
                cookie += 1
                if cookie == sl:
                    return idx
            cookie += 1
            if cookie == sl:
                return idx + 1
        return len(g)