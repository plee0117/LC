class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for ltr in s:
            if ltr in t[idx:]:
                idx += t[idx:].index(ltr) + 1
            else:
                return False
        return True