class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = dict()
        for i, l in enumerate(s):
            if l in sd:
                sd[l] += 1
            else:
                sd[l] = 1
        td = dict()
        for i, l in enumerate(t):
            if l in td:
                td[l] += 1
            else:
                td[l] = 1
        if sd == td:
            return True
        else: return False