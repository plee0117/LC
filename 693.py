class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = str(bin(n))[2:]
        if len(a) < 2:
            return True
        else:
            for idx, n in enumerate(a[:-1]):
                if n == a[idx + 1]:
                    return False
            return True