class Solution:
    def isUgly(self, num: int) -> bool:
        ugly = [1,2,3,5]
        if num < 1:
            return False
        else:
            while num not in ugly:
                if num % 2 == 0:
                    num = num // 2
                elif num % 3 == 0:
                    num = num // 3
                elif num % 5 == 0:
                    num = num // 5
                else:
                    return False
            return True