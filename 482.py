class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().replace('-','')
        f = len(S) % K
        groups = len(S) // K
        if f == 0:
            out = ''
        else:
            out = S[:f] + '-'
        idx = 0
        while idx < groups:
            out += S[idx * K + f: (idx + 1) * K + f] + '-'
            idx += 1
        return out[:-1]