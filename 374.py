# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n
        l = 1
        h = n
        t = (h + l)//2
        g = guess(t)
        while g != 0:
            if g > 0:
                l = t
            else:
                h = t
            t = (h + l)//2
            g = guess(t)
        return t