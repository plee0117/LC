class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xbin = str(bin(x)[2:])
        ybin = str(bin(y)[2:])
        if len(xbin) > len(ybin):
            ybin = '0' * (len(xbin) - len(ybin)) + ybin
            diff = sum(0 if dig == ybin[idx] else 1 for idx, dig in enumerate(xbin))
        else:
            xbin = '0' * (len(ybin) - len(xbin)) + xbin
            diff = sum(0 if dig == ybin[idx] else 1 for idx, dig in enumerate(xbin))
        return diff