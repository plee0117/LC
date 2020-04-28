class Solution:
    def arrangeCoins(self, n: int) -> int:
        idx = 0
        while 0 <= n:
            idx += 1
            n -= idx
        return idx - 1