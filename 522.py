class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        from collections import Counter
        
        def check(part, whole):
            idx = 0
            for ltr in part:
                lw = len(whole)
                inthere = False
                while idx < lw:
                    if ltr == whole[idx]:
                        inthere = True
                        idx += 1
                        break
                    else:
                        idx += 1
            return inthere
        
        c = Counter(strs)
        if len(c) == 1:
            return -1
        u = []
        r = []
        for k, v in c.items():
            if v == 1:
                u.append(k)
            else:
                r.append(k)
        if len(u) == 0:
            return -1
        elif len(r) == 0:
            u.sort(reverse = True, key = lambda x: len(x))
            return len(u[0])
        r.sort(reverse = True, key = lambda x: len(x))
        u.sort(reverse = True, key = lambda x: len(x))
        if len(u[0]) >= len(r[0]):
            return len(u[0])
        else:
            lenu = len(r)
            for item in u:
                idx = 0
                while idx < lenu:
                    if len(item) < len(r[idx]):
                        if item in r[idx]:
                            idx += 1
                        elif check(item,r[idx]):
                            idx += 1
                        else:
                            return len(item)
                    else:
                        break
        return -1