class Solution:
    def climbStairs(self, n: int) -> int:
        import math as m
        steps = 0
        ps = 0
        while 2 * ps <= n:
            si = n - 2 * ps
            steps += m.factorial(si + ps) // m.factorial(si) // m.factorial(ps)
            ps += 1
        return steps