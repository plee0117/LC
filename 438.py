class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pct = {}
        for ltr in p:
            if ltr in pct:
                pct[ltr] += 1
            else:
                pct[ltr] = 1
        lp = len(p)
        ls = len(s)
        if ls < lp:
            return []
        sct = {}
        for ltr in s[:lp]:
            if ltr in sct:
                sct[ltr] += 1
            else:
                sct[ltr] = 1
        out = []
        if pct == sct:
            out.append(0)
        idx = 0
        while idx + lp < ls:
            if sct[s[idx]] == 1:
                sct.pop(s[idx])
            else:
                sct[s[idx]] -= 1
            if s[idx + lp] in sct:
                sct[s[idx + lp]] += 1
            else:
                sct[s[idx + lp]] = 1

            if pct == sct:
                out.append(idx + 1)
            idx += 1
        return out