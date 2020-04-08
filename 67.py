class Solution:
    def addBinary(self, a: str, b: str) -> str:
        abin = 0
        bbin = 0
        for idx, num in enumerate(a[::-1]):
            abin += int(num)*(2**idx)
        for idx, num in enumerate(b[::-1]):
            bbin += int(num)*(2**idx)
        return bin(abin+bbin)[2:]