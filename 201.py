class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        mbin = str(bin(m))[2:]
        nbin = str(bin(n))[2:]
        l = len(mbin)
        if l < len(nbin):
            return 0
        else:
            sq = 0
            for idx, s in enumerate(mbin):
                if s == nbin[idx]:
                    if s == '1':
                        sq += 2 ** (l - idx - 1)
                else:
                    break
            return sq