class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        nums = 0
        for i in range(len(s)-1):
            if conv[s[i]] < conv[s[i + 1]]:
                nums -= conv[s[i]]
            else:
                nums += conv[s[i]]
        nums += conv[s[-1]]
        return nums