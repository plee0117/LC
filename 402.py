class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        peak = 0
        while k > 0 and peak + 1 < len(num):
            if num[peak] > num[peak + 1]:
                num = num[0:peak] + num[peak + 1:]
                peak = max(0, peak - 1)
                k -= 1
            else:
                peak += 1
        if k > 0:
            num = num[:-k]
        return str(int(num))