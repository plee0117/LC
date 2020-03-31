class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        fs = [1]
        factor = 2
        sq = num ** (1/2) // 1
        while factor <= sq :
            if num % factor == 0:
                fs.append(factor)
                fs.append(num//factor)
            factor += 1
        return sum(fs) == num