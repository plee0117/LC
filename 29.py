class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 1
        if dividend < 0:
            ans = -1
            dividend = -1 * dividend
        if divisor < 0:
            ans = -1 * ans
            divisor = -1 * divisor
        q = 0
        while dividend >= divisor:
            q += 1
            dividend -= divisor
        return ans * q