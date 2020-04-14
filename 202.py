class Solution:
    def isHappy(self, n: int) -> bool:
        tried = set()
        while True:
            s = 0
            for ltr in str(n):
                s += int(ltr)**2
            if s == 1:
                return True
            elif s in tried:
                return False
            else:
                tried.add(s)
            n = s