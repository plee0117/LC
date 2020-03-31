class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            neg = '-'
            num = -1 * num
        elif num > 0:
            neg = ''
        else:
            return '0'
        b7 = ''
        while num > 0:
            b7 = str(num % 7) + b7
            num = num // 7
        return neg + b7