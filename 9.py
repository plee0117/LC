class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        mpow = 0
        n = x
        while n>=10:
            n = n//10
            mpow += 1
        while mpow > 0:
            left = x // (10 ** (mpow))
            right = x % 10
            print(left, right)
            
            if left != right:
                return False
            x = x % (10 **(mpow)) // 10
            mpow -= 2
        return True