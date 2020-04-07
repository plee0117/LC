class Solution:
    def myAtoi(self, str: str) -> int:
        c = ''
        for i in str:
            if i == ' ':
                if c == '':
                    continue
                else:
                    break
            elif i in ['-','+']:
                if c == '':
                    c += i
                else:
                    break
            elif ord(i) >= ord('0') and ord(i) <= ord('9'):
                c += i
            else:
                break
        if c == '' or c == '-' or c == '+':
            return 0
        else:
            c = int(c)
            if c > 2**31 - 1:
                return 2**31 - 1
            elif c < -(2**31):
                return -(2**31)
            else:
                return c
                