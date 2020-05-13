class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        elif numRows == 1:
            return s
        elif len(s) <= numRows:
            return s
        grouped = {}
        gs = numRows * 2 - 2
        for i in range(len(s)):
            grem = i % gs
            if grem in grouped:
                grouped[grem].append(s[i])
            else:
                grouped[grem] = [s[i]]
        out = ''.join(grouped[0])
        for i in range(1, numRows - 1):
            ctr = 0
            if gs - i in grouped:
                length = len(grouped[gs - i])
                while ctr < length:
                    out += grouped[i][ctr]
                    out += grouped[gs - i][ctr]
                    ctr += 1
            if ctr < len(grouped[i]):
                out += grouped[i][ctr]
        out += ''.join(grouped[numRows - 1])
        return out