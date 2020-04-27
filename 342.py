class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        s = str(bin(num))[2:]
        # print(s)
        if len(s) % 2 == 0:
            return False
        elif '1' in s[1:]:
            return False
        else:
            return True