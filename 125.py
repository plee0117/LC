class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub('\W|_','',s)
        print(s)
        s = s.lower()
        print(s)
        h = len(s) // 2
        for i in range(h):
            print(s[i],s[-1-i])
            if s[i] != s[-1-i]:
                return False
        return True