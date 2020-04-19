class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            ns = str(num)
            num = 0
            for i in ns:
                num += int(i)
        return num