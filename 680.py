class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkP(s):
            idx = 0
            jdx = len(s) - 1
            while idx < jdx:
                if s[idx] == s[jdx]:
                    idx += 1
                    jdx -= 1
                else:
                    return (idx, jdx)
            return True
        first = checkP(s)
        if first == True:
            return True
        elif checkP(s[:first[0]] + s[first[0] + 1:]) == True:
            return True
        elif first[1] == len(s) - 1:
            if checkP(s[:first[1]]) == True:
                return True
        elif first[1] < len(s):
            if checkP(s[:first[1]] + s[first[1] + 1:]) == True:
                return True
        else:
            return False