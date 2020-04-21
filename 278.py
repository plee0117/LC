# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxf = 0
        mint = n
        while mint - maxf > 1:
            t = (mint + maxf) // 2
            if isBadVersion(t):
                mint = t
            else: maxf = t
        return mint