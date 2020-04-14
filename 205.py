class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = dict()
        td = dict()
        for i, l in enumerate(s):
            if l in sd:
                if t[i] in td:
                    if td[t[i]] != sd[l]:
                        return False
                    else:
                        td[t[i]].append(i)
                        sd[l].append(i)
                else:
                    return False
            elif t[i] in td:
                return False
            else:
                sd[l] = [i]
                td[t[i]] = [i]
        return True