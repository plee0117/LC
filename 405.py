class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 2 ** 32
        elif num == 0:
            return '0'
        ret = ''
        while num > 0:
            r = num % 16
            if r > 9:
                ret = 'abcdef'[r - 10] + ret
            else:
                ret = str(r) + ret
            num = num // 16
        return ret