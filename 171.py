class Solution:
    def titleToNumber(self, s: str) -> int:
        l = len(s) - 1
        n = 0
        for i, ltr in enumerate(s):
            n += (ord(ltr) - 64) * 26 ** (l - i)
        return n