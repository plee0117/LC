class Solution:
    def convertToTitle(self, n: int) -> str:
        cs = ''
        while n > 26:
            r = n % 26
            if r > 0:
                cs = chr(64 + r) + cs
                n = n // 26
            else:
                cs = 'Z' + cs
                n = n // 26 - 1
        if n > 0:
            cs = chr(64 + n) + cs
        return cs