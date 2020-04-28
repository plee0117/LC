class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if l1 > l2:
            sl = l2
            ll = l1
            sn = num2
            ln = num1
        else:
            sl = l1
            ll = l2
            sn = num1
            ln = num2
        carry = 0
        out = ''
        idx = 0
        while idx < sl:
            summed = int(sn[-1 - idx]) + int(ln[-1 - idx]) + carry
            carry = summed // 10
            out = str(summed % 10) + out
            idx += 1
        while idx < ll:
            summed = int(ln[-1 - idx]) + carry
            carry = summed // 10
            out = str(summed % 10) + out
            idx += 1
        if carry > 0:
            return str(carry) + out
        else:
            return out
        print(num1[-1 - len(num1)])