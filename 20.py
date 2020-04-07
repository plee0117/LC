class Solution:
    def isValid(self, s: str) -> bool:
        syms = []
        openers = ['(','{','[']
        closers = [')','}',']']
        for ltr in s:
            if ltr in openers:
                syms.append(ltr)
            elif len(syms) == 0:
                return False
            elif openers.index(syms[-1]) == closers.index(ltr):
                syms.pop()
            else:
                return False
        if len(syms) > 0:
            return False
        return True