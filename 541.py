class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        out = ''
        i = 0
        l = len(s)
        while True:
            if k * i >= l:
                break
            else:
                out += s[k * i: k * i + k][::-1]
            if k * i + k >= l:
                break
            else:
                out += s[k * i + k: k * (i + 2)]
            i += 2
        return out