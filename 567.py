class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        d1 = {}
        for ltr in s1:
            if ltr in d1:
                d1[ltr] += 1
            else:
                d1[ltr] = 1
        d2 = {}
        for ltr in s2[:l1]:
            if ltr in d2:
                d2[ltr] += 1
            else:
                d2[ltr] = 1
        if d1 == d2:
            return True
        idx = 0
        while idx + l1 < l2:
            if d2[s2[idx]] > 1:
                d2[s2[idx]] -= 1
            else:
                d2.pop(s2[idx])
            if s2[idx + l1] in d2:
                d2[s2[idx + l1]] += 1
            else:
                d2[s2[idx + l1]] = 1
            if d1 == d2:
                return True
            idx += 1
        return False