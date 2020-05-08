class Solution:
    def findComplement(self, num: int) -> int:
        return int(2 ** len(bin(num)[2:]) - num - 1)