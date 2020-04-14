class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))[2:]
        return sum(1 for i in s if i == '1')