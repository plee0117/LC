class Solution:
    def trailingZeroes(self, n: int) -> int:
        q = 0
        while n >= 5:
            q += n // 5
            n = n // 5
        return q